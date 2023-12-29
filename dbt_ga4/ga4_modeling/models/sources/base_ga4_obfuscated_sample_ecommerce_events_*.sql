with source as (
      select * from {{ source('ga4_obfuscated_sample_ecommerce', 'events_*') }}
),
renamed as (
    select
        

    from source
)
select * from renamed
  