import csv
from datetime import date
from datetime import datetime

#import datetime
import calendar


'''
date = "01/23/2024"
date = str(date)
print(date)
datetime_object = datetime.strptime(date, '%m/%d/%Y')
print(datetime_object.weekday())
'''

def switch(argument):
	switcher = {
		0: "Monday",
		1: "Tuesday",
		2: "Wednesday",
		3: "Thursday",
		4: "Friday",
		5: "Saturday",
		6: "Sunday"
	}
	return switcher.get(argument, "Invalid day of week")
#print(switch(1))


filename = "ScottDates.csv"
weekdaysList = []
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        date = row[0].strip()
        print(date) # 01/23/2024
        datetime_object = datetime.strptime(date, '%m/%d/%Y')
        day_of_week = datetime_object.weekday() # 0 = Monday, 6 = Sunday

		# Add day_of_week to list
        weekdaysList.append(switch(day_of_week))
        
        
        #print(datetime_object)
        #print(day_of_week)
        #print(switch(day_of_week))
        print(calendar.day_name[day_of_week])
        

print("Monday: " + str(weekdaysList.count("Monday")))
print("Tuesday: " + str(weekdaysList.count("Tuesday")))
print("Wednesday: " + str(weekdaysList.count("Wednesday")))
print("Thursday: " + str(weekdaysList.count("Thursday")))
print("Friday: " + str(weekdaysList.count("Friday")))
print("Saturday: " + str(weekdaysList.count("Saturday")))
print("Sunday: " + str(weekdaysList.count("Sunday")))

