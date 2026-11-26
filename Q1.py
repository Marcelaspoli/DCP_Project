# Question 1: Does consuming caffeine at night change how late I fall asleep or how good my sleep quality is?


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/sleep_habits.csv")

# Convert bedtime into numerical hours
bedtime = pd.to_datetime(df["bed_time"], format="%H:%M")
df["bed_hour"] = bedtime.dt.hour + bedtime.dt.minute / 60

# Treat times after midnight as later bedtimes
df.loc[df["bed_hour"] < 12, "bed_hour"] += 24

# Compare averages with and without caffeine
results = df.groupby("caffeine_night")[["bed_hour", "sleep_quality_1_5"]].mean()
results = results.rename(index={0: "No caffeine", 1: "Caffeine"})

print(results.round(2))

# Calculate differences
bed_diff = results["bed_hour"].diff().iloc[-1] * 60
quality_diff = results["sleep_quality_1_5"].diff().iloc[-1]

print(f"Bedtime difference: {bed_diff:.1f} minutes")
print(f"Sleep quality difference: {quality_diff:.2f}")

# Plot average bedtime
results["bed_hour"].plot(kind="bar", rot=0)
plt.title("Effect of Nighttime Caffeine on Bedtime")
plt.ylabel("Average bedtime")
plt.xlabel("")
plt.yticks(range(20, 29), [f"{h % 24:02d}:00" for h in range(20, 29)])
plt.ylim(20, 28)
plt.tight_layout()
plt.savefig("images/caffeine_bedtime.png", dpi=300)
plt.show()

# Plot average sleep quality
results["sleep_quality_1_5"].plot(kind="bar", rot=0)
plt.title("Effect of Nighttime Caffeine on Sleep Quality")
plt.ylabel("Average sleep quality")
plt.xlabel("")
plt.ylim(0, 5)
plt.tight_layout()
plt.savefig("images/caffeine_sleep_quality.png", dpi=300)
plt.show()