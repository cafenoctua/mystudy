with
import_stg as (
  select *
  from {{ ref('stg__events') }}
  {% if not(var('backfill')) -%}
  where
    date(event_timestamp) = "{{ var('date') }}"
  {%- endif %}
),

get_daily_values as (
  select
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
    import_stg
  group by 1, 2, 3, 4, 5, 6, 7, 8, 9
)

select 
  {{ dbt_utils.generate_surrogate_key(['user_id', 'created_at', 'updated_at']) }} as user_key,
  user_id,
  created_at,
  platform,
  category,
  mobile_brand_name,
  mobile_model_name,
  operating_system,
  operating_system_version,
  device_language,
  updated_at
from
  get_daily_values