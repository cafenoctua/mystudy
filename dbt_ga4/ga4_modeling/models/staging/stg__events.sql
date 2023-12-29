with
source as (
    select * from {{ source('ga4_obfuscated_sample_ecommerce', 'events_*') }}
),
renamed as (
    select
        event_timestamp,
        event_name,
        user_id,
        user_pseudo_id,
        user_first_touch_timestamp,
        platform,
        device,
        geo,
        app_info
    from
        source
)

select * from renamed
  