# weekday.py
# Author : Adedoyinsola Fifo
## weekdays


import datetime

now = datetime.datetime.now()

# Get the day of the week (0 = Monday, 1 = Tuesday, etc.)
day_of_week = now.weekday()

# Check if today is a weekday (i.e., not Saturday or Sunday)
if day_of_week < 5:
    print("Today is a weekday.")
else:
    print("Today is not a weekday.")
