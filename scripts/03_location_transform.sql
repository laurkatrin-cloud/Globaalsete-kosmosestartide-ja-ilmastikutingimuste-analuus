CREATE SCHEMA IF NOT EXISTS mart;

DROP TABLE IF EXISTS mart.launches_by_location;

CREATE TABLE mart.launches_by_location AS
SELECT
    location_name,
    COUNT(*) AS launch_count
FROM staging.launches_raw
WHERE location_name IS NOT NULL
GROUP BY location_name
ORDER BY launch_count DESC;
