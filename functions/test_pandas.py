import pandas as pd
import numpy as np
from datetime import datetime

#filename = "Python\\Practice\\jobs_in_data.csv\\jobs_in_data.csv"
#filename = "Python\Practice\jobs_in_data.csv"
filename = "C:\\Users\\brenn\\OneDrive\Documents\\__Repo\\CB\\Python\\Practice\\jobs_in_data.csv"

f = open(filename)
#print(f.read())

df = pd.read_csv(filename)
cols = ["work_year", "job_title"]
airbnb_data = pd.read_csv(filename, index_col=0, usecols=cols)

print(df.head())
#df.head()
#print(df)
