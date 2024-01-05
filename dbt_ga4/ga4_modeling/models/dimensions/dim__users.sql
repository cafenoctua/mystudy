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
    date(event_timestamp) date,
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
  group by 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
)

select 
  {{ dbt_utils.generate_surrogate_key(['user_id', 'created_at', 'updated_at']) }} as user_key,
  *
from
  get_daily_values