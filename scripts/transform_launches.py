import json
import pandas as pd
import os

with open("data/raw/upcoming_launches.json", "r") as f:
    data = json.load(f)

launches = data["results"]

companies = []

for launch in launches:
    provider = launch["launch_service_provider"]["name"]
    companies.append(provider)

df = pd.DataFrame(companies, columns=["company"])

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
