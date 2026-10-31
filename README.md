#  Night-Time Routine & Next-Day Wake-Up Analysis

**Data-Centric Programming Project**

A personal dataset tracking my night-time routine, built to find out whether anything I do in the evening affects how I wake up the next day.

---

## Project Goal

To analyse whether parts of my routine (what I eat, when I eat, caffeine, and when I go to sleep) have an effect on my next-morning outcomes: how I feel when I wake up, whether I snooze, and whether I end up late.

### Questions to explore

- Does **caffeine at night** change how late I fall asleep or how I feel in the morning?
- Do **healthy meals** vs **fast food** lead to different moods the next day?
- Does eating **later at night** affect my sleep time or wake-up mood?
- Does the type of day (**University**, **Free** or **Work**) change my sleep and wake-up patterns?
- Which factors are most linked to **snoozing** or being **late**?

---

## Dataset

The data is collected from my own daily routine, with one row per night.

| Column | Description | Values |
|--------|-------------|--------|
| `Date` | Date of the entry | DD/MM |
| `Day Type` | What kind of day it was | University, Free, Work |
| `Meal` | Type of meal eaten | Healthy, Fast food |
| `Meal Time` | Time the meal was eaten | e.g. 20:30 |
| `Caffeine at night` | Whether I had caffeine in the evening | Y, N |
| `Sleep time` | Time I went to sleep | e.g. 23:45 |
| `Wake up time` | Time I woke up | e.g. 07:30 |
| `Mood` | How I felt on waking up | Sleepy, Energised |
| `Snooze` | Whether I snoozed my alarm | Y, N |
| `Late` | Whether I was late to start my day| Y, N |

**Inputs (the evening before):** Day Type, Meal, Meal Time, Caffeine at night, Sleep time
**Outcomes (the next morning):** Wake up time, Mood, Snooze, Late


## Notes

This is a small, self-collected dataset, so the results show patterns in my own routine rather than general conclusions. 
