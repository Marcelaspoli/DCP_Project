import os
import datetime as dt
import pandas as pd

SRC = "DCP_dataset.xlsx"
DST = "data/sleep_habits.csv"


df = pd.read_excel(SRC, sheet_name=0).replace("", pd.NA)

# format time and date for readability in CSV
def fmt(v):
    if isinstance(v, dt.time):
        return v.strftime("%H:%M")
    if isinstance(v, (dt.datetime, dt.date)):
        return v.strftime("%Y-%m-%d")
    return v

df = df.apply(lambda col: col.map(fmt))

os.makedirs("data", exist_ok=True)
df.to_csv(DST, index=False)
print(f"Wrote {len(df)} rows to {DST}")