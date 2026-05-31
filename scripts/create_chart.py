import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv(
    "data/processed/company_launch_counts.csv"
)

top5 = df.head(5)

plt.figure(figsize=(8,5))

plt.bar(
    top5["company"],
    top5["launches"]
)

plt.xticks(rotation=45)
plt.title("TOP 5 ettevõtet startide arvu järgi")
plt.tight_layout()

os.makedirs("output", exist_ok=True)

plt.savefig(
    "output/top_companies.png"
)

print("Graafik loodud.")
