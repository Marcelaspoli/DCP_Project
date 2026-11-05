# Data Centric Programming Assignment 2026

https://github.com/skooter500/dcp26-assignment/blob/main/dataset_assignment.md

A personal dataset tracking my night-time routine, built to find out whether anything I do in the evening affects how I wake up the next day.

# Questions 

- Does **caffeine at night** change how late I fall asleep or how good my sleep was?
- Do **healthy meals** vs **fast food** lead to different sleep quality?
- Does eating **later at night** affect my sleep time or sleep quality?
- Does the type of day (**University**, **Free** or **Work**) change my sleep and wake-up patterns?
- Which factors are most linked to **snoozing** or being **late**?

# Data Dictionary

The data is recorded in `data/sleep_habits.csv` (the same data also lives in `DCP_dataset.xlsx`). One row per night, logged every morning.

| Column | Type | Units / values | How it is measured |
|--------|------|----------------|--------------------|
| `date` | date | YYYY-MM-DD | Calendar date of the entry |
| `weekday` | text | Mon-Sun | Calculated from `date` |
| `day_type` | category | University, Free, Work | What kind of day it was |
| `dinner_type` | category | Healthy, Fast food | Type of my last main meal of the day (Healthy = home-cooked meal, Fast food = takeaway or fast food) |
| `dinner_time` | time | HH:MM, 24-hour (e.g. 20:30) | Time I started eating that meal. 00:00 is midnight |
| `caffeine_night` | binary | 0 = no, 1 = yes | 1 if I had any caffeine in the evening (after 18:00) |
| `bed_time` | time | HH:MM, 24-hour (e.g. 23:45) | Time I went to sleep on the night of this date. Times after midnight (e.g. 01:00) belong to the night of this date |
| `wake_time` | time | HH:MM, 24-hour (e.g. 07:30) | Time I woke up the next morning |
| `sleep_hrs` | number | hours, 1 decimal (e.g. 8.0) | Calculated: time from `bed_time` to `wake_time`, handling midnight |
| `hrs_dinner_to_bed` | number | hours, 1 decimal (e.g. 5.0) | Calculated: time from `dinner_time` to `bed_time` |
| `sleep_quality` | integer | 1 (poor) to 5 (great) | My own rating of how good my sleep was, given each morning |
| `snoozed` | binary | 0 = no, 1 = yes | 1 if I snoozed my alarm that morning |
| `late` | binary | 0 = no, 1 = yes | 1 if I was late to start my day (arrived after the planned start time) |

**Inputs (the evening before):** date, weekday, day_type, dinner_type, dinner_time, caffeine_night
**Outcomes (the next morning):** bed_type, wake_time, sleep_hrs, hrs_dinner_to_bed, sleep_quality, snoozed, late

**Rules I follow when recording:**
- One row per day. If I miss a day, the row stays and the cells are left blank.
- I log every morning at the same time, so I don't reconstruct from memory.
- All times use the 24-hour format.
- Data collection started on 19 October 2026.
  
# Description of the project

I built my own dataset by recording my evening routine (dinner, caffeine, bedtime) and how I woke up the next day. I then analyse it to see which parts of my routine are linked to my sleep and my mornings.

# Instructions for use

1. Clone the repository: `git clone https://github.com/Marcelaspoli/DCP_Project.git`
2. Open `data/sleep_habits.csv` for the raw data, or `DCP_dataset.xlsx` for the spreadsheet version with dropdowns and formulas.
3. Run the analysis: `python main.py`

# How it works:

Each morning I add a new row to the Excel sheet. Dropdowns keep the categories consistent, and formulas calculate `weekday`, `sleep_hrs` and `hrs_dinner_to_bed`. I then export the sheet to CSV and commit both files to GitHub, so the repository has a dated record of my data collection.

# Findings



# List of files in the project

| Files | Source |
|-----------|-----------|
| README.md | Self written |
| DCP_dataset.xlsx | Self written (spreadsheet with dropdowns and formulas) |
| data/sleep_habits.csv | Self written (CSV export of the spreadsheet) |
| main.py | Self written |

# References
My own daily routine.

# What I am most proud of in the assignment



# What I learned

