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
    geo.continent,
    geo.sub_continent,
    geo.country,
    geo.region,
    geo.city,
    max(event_timestamp) as updated_at
  from
    import_stg
  group by 1, 2, 3, 4, 5, 6
)

select 
  {{ dbt_utils.generate_surrogate_key(['continent','sub_continent','country','region','city','updated_at']) }} as country_key,
  *
from
  get_daily_values