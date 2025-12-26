#import csv




#file = open("Python\Practice\jobs_in_data.txt", "r",newline='')
#print(file.read())

# txt = file.readline()
# for row in txt:
# 	print("row: " + str(row))
# print(txt)

def read_file(filename):
	file = open(filename, "r")
	while True:
		line = file.readline()
		if not line:
			break
		print(line)
	file.close()

filename = "Python\Practice\jobs_in_data.csv"
#read_file(filename)

import csv
with open(filename, 'r', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	#print(spamreader)
	for row in spamreader:
		print(row)
		break
		#print(', '.join(row))



# import pandas as pd
# df = pd.read_csv('Practicejobs_in_data.csv')