# Dates
from datetime import date, timedelta, datetime

today = date.today()
print(today)

formatted_date = today.strftime("%A %d-%m-%Y")  # 19-01-2024
print(formatted_date)

after_forty_days = today + timedelta(days=40)  # crt + click
print(after_forty_days)

dob = "1999-08-17"
# convert to date
date_of_birth = datetime.strptime(dob, "%Y-%m-%d")
age = today.year - date_of_birth.year
print("I am", age, "years old")

age_in_days = datetime.today() - date_of_birth
print(age_in_days.days//365)  #in years
print(age_in_days.days) # in days

#python changle