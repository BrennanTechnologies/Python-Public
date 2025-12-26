import os
import csv

#dir = "C:\\Users\\brenn\\OneDrive\\Documents\\_Scott"
dir = "."
file = "ScottDates.csv"
filePath = dir + "\\" + file
print(filePath)
print (sorted(os.listdir(dir)))

file = open(filePath,'r')
file = file.read()
reader = csv.reader(file, delimiter=',')
#print(reader)

for row in reader:
	print(row)

	