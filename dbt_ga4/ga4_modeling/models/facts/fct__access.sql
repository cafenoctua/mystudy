with
import_stg as (
  select *
  from {{ ref('stg__events') }}
  {% if not(var('backfill')) -%}
  where
    date(event_timestamp) = "{{ var('date') }}"
  {%- endif %}
),

import_dim_users as (
  select *
  from {{ ref('dim__users') }}
  {% if not(var('backfill')) -%}
  where
    date(updated_at) = "{{ var('date') }}"
  {%- endif %}
),

import_dim_countries as (
  select *
  from {{ ref('dim__countries') }}
  {% if not(var('backfill')) -%}
  where
    date(updated_at) = "{{ var('date') }}"
  {%- endif %}
)

select
  import_dim_users.user_key,
  import_dim_countries.country_key,
  import_stg.event_timestamp as access_timestamp,
  import_stg.event_timestamp
from 
  import_stg
inner join 
  import_dim_users
  on 
    import_stg.user_id = import_dim_users.user_id
    and import_stg.created_at = import_dim_users.created_at
    and date(import_stg.event_timestamp) = date(import_dim_users.updated_at)
inner join 
  import_dim_countries
  on 
    import_stg.geo.continent = import_dim_countries.continent
    and import_stg.geo.sub_continent = import_dim_countries.sub_continent
    and import_stg.geo.country = import_dim_countries.country
    and import_stg.geo.region = import_dim_countries.region
    and import_stg.geo.city = import_dim_countries.city
    and date(import_stg.event_timestamp) = date(import_dim_countries.updated_at)