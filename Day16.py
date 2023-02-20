	#Exercises: Day 16
#Q1. Get the current day, month, year, hour, minute and timestamp from datetime module

import datetime

# get current date and time
now = datetime.datetime.now()

# extract individual components
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()

# print results
print(" Your Current date and time is now: ", now)
print("Day: ", day)
print("Month: ", month)
print("Year: ", year)
print("Hour: ", hour)
print("Minute: ", minute)
print("Timestamp: ", timestamp)

#Q2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")

import datetime

# get current date and time
now = datetime.datetime.now()

# extract individual components
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second

# format the date and time
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")

# print results
print("Current date and time: ", formatted_date)



#Q3. Today is 5 December, 2019. Change this time string to time.


import datetime

date_string = "5 December, 2019"

# use strptime to convert the string to a datetime object
date_obj = datetime.datetime.strptime(date_string, "%d %B, %Y")

# print the resulting datetime object
print(date_obj)


#Q4. Calculate the time difference between now and new year.


import datetime

# Get the current date and time
now = datetime.datetime.now()

# Calculate the difference between now and New Year's Day
new_year = datetime.datetime(now.year + 1, 1, 1)
time_difference = new_year - now

# Print the time difference in days, hours, and minutes
print(" New Year from now on, is:", time_difference.days, "days and", time_difference.seconds // 3600, "hours and", (time_difference.seconds // 60) % 60, "minutes")


#Q5. Calculate the time difference between 1 January 1970 and now.

import datetime

# Get the current date and time
now = datetime.datetime.now()

# Create a datetime object previous
previous = datetime.datetime(1970, 1, 1)

# Calculate the time difference between previous and now
time_difference = now - previous

# Print the time difference in seconds
print("Time diffrence from 1970,1,1 to date is :", time_difference.total_seconds(), "seconds")


#Q6. Think, what can you use the datetime module for? 

# Some of the common use cases for the datetime module include:

Time series analysis.
Parsing and formatting dates and times:
Calculating time intervals:
Timezone and daylight saving time handling: 
Date arithmetic: 
Event scheduling and reminders: 
Working with timestamps: 


