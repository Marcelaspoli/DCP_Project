#  Night-Time Routine & Next-Day Wake-Up Analysis

**Data-Centric Programming Project**

A personal dataset tracking my night-time routine, built to find out whether anything I do in the evening affects how I wake up the next day.

---

## Project Goal

To analyse whether parts of my routine have an effect on my next-morning outcomes: my sleep quality, whether I snooze, and whether I end up late to start my day. 

### Questions to explore

- Does **caffeine at night** change how late I fall asleep or how good my sleep was?
- Do **healthy meals** vs **fast food** lead to different sleep quality?
- Does eating **later at night** affect my sleep time or sleep quality?
- Does the type of day (**University**, **Free** or **Work**) change my sleep and wake-up patterns?
- Which factors are most linked to **snoozing** or being **late**?

---

## Dataset

The data is collected from my own daily routine, with one row per night.

| Column | Description | Values |
|--------|-------------|--------|
| `date` | Date of the entry | YY/DD/MM |
| `weekday` | Day of the week | Sun-Sat |
| `day_type` | What kind of day it was | University, Free, Work |
| `dinner_type` | Type of meal eaten | Healthy, Fast food |
| `dinner_time` | Time the meal was eaten | e.g. 20:30 |
| `caffeine_night` | Whether I had caffeine in the evening | 0, 1 |
| `bed_time` | Time I went to sleep | e.g. 23:45 |
| `wake_time` | Time I woke up | e.g. 07:30 |
| `sleep_hrs` | How many hours of sleep I had | e.g. 8.0 |
| `hrs_dinner_to_bed` | How much time from dinner to bed | e.g. 5.0 |
| `sleep_quality` | How good was my sleep | 1-5 |
| `snoozed` | Whether I snoozed my alarm | 0, 1 |
| `late` | Whether I was late to start my day| 0, 1 |

**Inputs (the evening before):** date, weekday, day_type, dinner_type, dinner_time, caffeine_night
**Outcomes (the next morning):** bed_type, wake_time, sleep_hrs, hrs_dinner_to_bed, sleep_quality, snoozed, late


## Notes

This is a small, self-collected dataset, so the results show patterns in my own routine rather than general conclusions. 
