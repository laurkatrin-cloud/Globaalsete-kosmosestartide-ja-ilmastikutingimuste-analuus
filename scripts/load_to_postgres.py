import json
import pandas as pd
from sqlalchemy import create_engine, text

RAW_FILE = "data/raw/upcoming_launches.json"

engine = create_engine(
    "postgresql://praktikum:praktikum@localhost:55432/kosmos"
)

with open(RAW_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

rows = []

for launch in data["results"]:
    pad = launch.get("pad") or {}
    location = pad.get("location") or {}
    provider = launch.get("launch_service_provider") or {}
    status = launch.get("status") or {}

    rows.append({
        "launch_id": launch.get("id"),
        "launch_name": launch.get("name"),
        "launch_status": status.get("name"),
        "net": launch.get("net"),
        "provider_name": provider.get("name"),
        "pad_name": pad.get("name"),
        "location_name": location.get("name"),
        "latitude": pad.get("latitude"),
        "longitude": pad.get("longitude"),
    })

df = pd.DataFrame(rows)

with engine.begin() as conn:
    conn.execute(text("CREATE SCHEMA IF NOT EXISTS staging"))

df.to_sql(
    "launches_raw",
    engine,
    schema="staging",
    if_exists="replace",
    index=False
)

print(f"Laetud PostgreSQL-i {len(df)} rida tabelisse staging.launches_raw")
