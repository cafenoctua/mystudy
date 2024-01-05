{% snapshot dim_scd__users %}

{{
  config(
    target_schema=target.schema,
    target_database=target.project,
    unique_key="user_key",
    strategy="timestamp",
    updated_at="updated_at"
  )
}}

with
base as (
  select
    {{ dbt_utils.generate_surrogate_key(['user_id', 'created_at']) }} as user_key,
    user_id,
    created_at,
    platform,
    device.category,
    device.mobile_brand_name,
    device.mobile_model_name,
    device.operating_system,
    device.operating_system_version,
    device.language as device_language,
    max(event_timestamp) as updated_at
  from
    {{ ref('stg__events') }}
  where
    date(event_timestamp) = "{{ var('date') }}"
  group by 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
)

select
  base.*
from
  base
left join
  {{ this }} as prev_dim
  on
    base.user_key = prev_dim.user_key
where
  prev_dim.user_key is null
  or (
    base.platform || base.category || base.mobile_brand_name || base.operating_system || base.operating_system_version || base.device_language !=
      prev_dim.platform || prev_dim.category || prev_dim.mobile_brand_name || prev_dim.operating_system || prev_dim.operating_system_version || base.device_language
  )
{% endsnapshot %}