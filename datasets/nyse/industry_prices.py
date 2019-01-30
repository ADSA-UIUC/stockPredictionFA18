import numpy as np;
import pandas as pd;

df=pd.read_csv("OP_NYSE.csv");

df=df[["Open","Close","Low","High","GICS Sub Industry"]]; #Open the csv file and reads in the prices and sub industries

df=df.values;

industry_map={};# creats two empty hash maps to calculate the average by summing the prices and dividing by the number of data points
industry_num={};

for row in df:
	industry=row[4];
	average= (row[0]+row[1]+row[2]+row[3])/4;	#Calculate the average. May change if better methodology determined
	if industry in industry_map: #If in the industry_map adds to the running usm
		industry_map[industry]=industry_map[industry]+average
		industry_num[industry]=industry_num[industry]+1;
	else:
		industry_map[industry]=average; #Initilizes values in the hash maps if otherwise.
		industry_num[industry]=1;
		
for key in industry_map: #Divides running sum by the number of data points for that category
	industry_map[key]= round(industry_map[key]/industry_num[key],2);

sorted_by_value = sorted(industry_map.items(), key=lambda kv: kv[1]); #Sorts hash_map

for key,value in sorted_by_value: # prints sorted_by_value out
	print(key,value);