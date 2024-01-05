with
source as (
  select * from {{ source('ga4_obfuscated_sample_ecommerce', 'events_*') }}
),
renamed as (
  select
    timestamp_micros(event_timestamp) as event_timestamp,
    event_name,
    user_pseudo_id as user_id,
    timestamp_micros(user_first_touch_timestamp) as created_at,
    platform,
    device,
    geo
  from
    source
)

select * from renamed