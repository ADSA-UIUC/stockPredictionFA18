import csv;
import pandas as pd;
import numpy as np;

security_df=pd.read_csv("securities.csv");

security=security_df[["Ticker symbol","GICS Sector","GICS Sub Industry"]];

security=security.values;

sector_map={};
sub_map={};

for row in security:
	symbol=row[0];
	sector=row[1];
	sub=row[2];	
	
	sector_map[symbol]=sector;
	sub_map[symbol]=sub;

#print(sector_map);
#print(sub_map);
	
	
new_df=pd.read_csv("new_new_fundamentals.csv");
new_df=new_df["Ticker Symbol"];
new_df=new_df.values;


sector_list=[];
sub_list=[];

for row in new_df:
	if row in sector_map:
		print(row);
		sector_list.append(sector_map[row]);
		sub_list.append(sub_map[row]);
	else:
		sector_list.append("Unknown");
		sub_list.append("Unknown");

new_df=pd.read_csv("new_new_fundamentals.csv");
new_df["GICS Sector"]=pd.Series((v for v in sector_list));
new_df["GICS Sub Industry"]=pd.Series((v for v in sub_list));

new_df.to_csv("OP_NYSE.csv");
	




