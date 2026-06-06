CREATE SCHEMA IF NOT EXISTS mart;

DROP TABLE IF EXISTS mart.launches_by_location_company;

CREATE TABLE mart.launches_by_location_company AS
SELECT
    location_name,
    provider_name,
    COUNT(*) AS launch_count
FROM staging.launches_raw
WHERE location_name IS NOT NULL
  AND provider_name IS NOT NULL
GROUP BY location_name, provider_name
ORDER BY launch_count DESC;
