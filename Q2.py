# Question 2: Does a healthy dinner improve sleep quality compared to fast food?

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/sleep_habits.csv")

# Remove unnecessary spaces (cleaning data) 
df["dinner_type"] = df["dinner_type"].str.strip()

# Compare average sleep quality by dinner type
results = df.groupby("dinner_type")["sleep_quality_1_5"].mean()

print(results.round(2))

# Calculate the difference in sleep quality
quality_diff = results["Healthy"] - results["Fast food"]

print(f"Sleep quality difference: {quality_diff:.2f}")

# Plot average sleep quality for each dinner type
results.plot(kind="bar", rot=0, color=["salmon", "lightgreen"])

plt.title("Dinner Type and Sleep Quality")
plt.ylabel("Average sleep quality")
plt.xlabel("Dinner type")
plt.ylim(0, 5)
plt.tight_layout()
plt.savefig("images/dinner_sleep_quality.png", dpi=300)
plt.show()