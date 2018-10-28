import csv;
import pandas as pd;
import numpy as np;

def add_company(prices_map,symbol,time):
	if symbol in prices_map:
		prices_map[symbol].append(time);
	else:
		prices_map[symbol]=[];

prices_df=pd.read_csv("prices.csv");
fundementals_df=pd.read_csv("fundamentals.csv");

prices=prices_df[["symbol","date"]];

prices=prices.values;

prices_map={};

for row in prices:
	symbol=row[0];
	time=row[1];
	
	add_company(prices_map,symbol,time);

#print(prices_map["WLTW"]);

new_fundementals=[];

old_fundementals=fundementals_df.values;

for row in old_fundementals:
	symbol=row[1];
	date=row[2];
	#print(symbol);
	if symbol in prices_map:
		if date in prices_map[symbol]:
			new_fundementals.append(row);

print(new_fundementals);
column_names=list(fundementals_df.columns.values)

new_df = pd.DataFrame(new_fundementals)
new_df.columns=column_names;
#new_df.to_csv("new_fundamentals.csv")

open=[];
close=[];
low=[];
high=[];
volume=[];
count=0;
for row in new_fundementals:
	count+=1;
	print(count);
	symbol=row[1];
	date=row[2];
	df_2_add=prices_df[prices_df.symbol==symbol];
	df_2_add=df_2_add[prices_df.date==date];
	df_2_add=df_2_add.values;
	df_2_add=df_2_add[0];
	open.append(df_2_add[2]);
	close.append(df_2_add[3]);
	low.append(df_2_add[4]);
	high.append(df_2_add[5]);
	volume.append(df_2_add[6]);

new_df["Open"]=pd.Series((v for v in open));
new_df["Close"]=pd.Series( (v for v in close) );
new_df["Low"]=pd.Series((v for v in low));
new_df["High"]=pd.Series((v for v in high));
new_df["Volume"]=pd.Series((v for v in volume));

new_df.to_csv("new_new_fundamentals.csv")


	