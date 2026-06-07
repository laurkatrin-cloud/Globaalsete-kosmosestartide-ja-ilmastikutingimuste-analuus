import json
import os
import pandas as pd

with open("data/raw/upcoming_launches.json", "r") as f:
    data = json.load(f)

launches = data["results"]

rows = []

for launch in launches:
    provider = launch["launch_service_provider"]["name"]
    net = launch["net"]

    rows.append({
        "company": provider,
        "net": net
    })

df = pd.DataFrame(rows)

df["net"] = pd.to_datetime(df["net"], utc=True)

today = pd.Timestamp.now(tz="UTC")
limit_date = today + pd.Timedelta(days=30)

df = df[
    (df["net"] >= today) &
    (df["net"] <= limit_date)
]

result = (
    df.groupby("company")
      .size()
      .reset_index(name="launches")
      .sort_values("launches", ascending=False)
)

os.makedirs("data/processed", exist_ok=True)

result.to_csv(
    "data/processed/company_launch_counts.csv",
    index=False
)

print(result.head())