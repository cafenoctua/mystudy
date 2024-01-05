{% snapshot dim_scd__countries %}

{{
  config(
    target_schema=target.schema,
    target_database=target.project,
    unique_key="country_key",
    strategy="timestamp",
    updated_at="updated_at"
  )
}}

with
base as (
  select
    {{ dbt_utils.generate_surrogate_key(['geo.continent','geo.sub_continent','geo.country','geo.region','geo.city']) }} as country_key,
    geo.continent,
    geo.sub_continent,
    geo.country,
    geo.region,
    geo.city,
    max(event_timestamp) as updated_at
  from
    {{ ref('stg__events') }}
  where
    date(event_timestamp) = "{{ var('date') }}"
  group by 1, 2, 3, 4, 5, 6
)

select
  base.*
from
  base
left join
  {{ this }} as prev_dim
  on
    base.country_key = prev_dim.country_key
where
  prev_dim.country_key is null
{% endsnapshot %}