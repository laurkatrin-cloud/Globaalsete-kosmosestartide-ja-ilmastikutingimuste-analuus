-- Test 1: Kontrollib, et launch_id ei oleks puuduv
SELECT COUNT(*) AS missing_launch_id
FROM staging.launches_raw
WHERE launch_id IS NULL;

-- Test 2: Kontrollib, et launch_id väärtused oleksid unikaalsed
SELECT COUNT(*) AS duplicate_launch_ids
FROM (
    SELECT launch_id
    FROM staging.launches_raw
    GROUP BY launch_id
    HAVING COUNT(*) > 1
) t;

-- Test 3: Kontrollib, et provider_name ei oleks puuduv
SELECT COUNT(*) AS missing_provider
FROM staging.launches_raw
WHERE provider_name IS NULL;

-- Test 4: Kontrollib, et ettevõtte startide arv oleks positiivne
SELECT COUNT(*) AS invalid_company_launch_count
FROM mart.company_launches
WHERE launch_count <= 0;

-- Test 5: Kontrollib, et asukoha startide arv oleks positiivne
SELECT COUNT(*) AS invalid_location_launch_count
FROM mart.launches_by_location
WHERE launch_count <= 0;

-- Test 6: Kontrollib, et ilmaandmetes oleks tuulekiirus olemas
SELECT COUNT(*) AS missing_wind_speed
FROM staging.weather_raw
WHERE wind_speed_ms IS NULL;

-- Test 7: Kontrollib, et ilmastikuriski skoor jääks vahemikku 0–100
SELECT COUNT(*) AS invalid_weather_risk_score
FROM mart.weather_risk
WHERE weather_risk_score < 0
   OR weather_risk_score > 100;