with
import_stg as (
  select * from {{ ref('stg__events') }} where date(event_timestamp) = "{{ var('date') }}"
),

import_dim_users as (
  select * from {{ ref('dim_scd__users') }} where date(dbt_valid_from) <= "{{ var('date') }}"
),

import_dim_countries as (
  select * from {{ ref('dim_scd__countries') }} where date(dbt_valid_from) <= "{{ var('date') }}"
),

get_latest_dim_users as (
  select
    import_dim_users.*
  from
    import_dim_users
  inner join
    (
      select
        user_key,
        max(dbt_valid_from) latest_from
      from
        import_dim_users
      group by 1
    ) as latest_data
    on
      import_dim_users.user_key = latest_data.user_key
      and import_dim_users.dbt_valid_from = latest_data.latest_from
),

get_latest_dim_countries as (
  select
    import_dim_countries.*
  from
    import_dim_countries
  inner join
    (
      select
        country_key,
        max(dbt_valid_from) latest_from
      from
        import_dim_countries
      group by 1
    ) as latest_data
    on
      import_dim_countries.country_key = latest_data.country_key
      and import_dim_countries.dbt_valid_from = latest_data.latest_from
)

select
  get_latest_dim_users.user_key,
  get_latest_dim_countries.country_key,
  import_stg.event_timestamp as access_timestamp,
  import_stg.event_timestamp
from 
  import_stg
inner join 
  get_latest_dim_users
  on 
    import_stg.user_id = get_latest_dim_users.user_id
    and import_stg.created_at = get_latest_dim_users.created_at
inner join 
  get_latest_dim_countries
  on 
    import_stg.geo.continent = get_latest_dim_countries.continent
    and import_stg.geo.sub_continent = get_latest_dim_countries.sub_continent
    and import_stg.geo.country = get_latest_dim_countries.country
    and import_stg.geo.region = get_latest_dim_countries.region
    and import_stg.geo.city = get_latest_dim_countries.city