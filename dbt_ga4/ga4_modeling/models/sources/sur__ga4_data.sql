SELECT
    *
FROM
    {{ source('ga4_obfuscated_sample_ecommerce', 'events_*') }}