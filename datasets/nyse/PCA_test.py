import numpy as np;
import pandas as pd;
from sklearn.decomposition import PCA;
from sklearn.preprocessing import StandardScaler



df=pd.read_csv("OP_NYSE.csv"); #Removes all non numeric columns from the data frame
df=df.loc[:, df.columns != 'Unnamed: 0.1'];
df=df.loc[:, df.columns != 'Ticker Symbol'];
df=df.loc[:, df.columns != 'Period Ending'];
df=df.loc[:, df.columns != 'GICS Sector'];
df=df.loc[:, df.columns != 'GICS Sub Industry'];

df=df.dropna(axis='rows');

open_array=df["Open"].values #find the values in of the pricing categories
close_array=df["Close"].values
low_array=df["Low"].values;
high_array=df["High"].values;


average_array=np.add(open_array,close_array); #adds the array together and takes their average
average_array=np.add(average_array,low_array);
average_array=np.add(average_array,high_array);
average_array=average_array/4;


columns=df.columns




x = StandardScaler().fit_transform(df);







pca=PCA(n_components=3);
pca.fit(df);

array=pca.fit_transform(df);
#print(array[:,0]);




test_map={};
for i in range(len(columns)):
	test_array=df[columns[i]]; #Finds the values for the specified factor
	correlation=np.corrcoef(test_array,array[:,0])[1,0]; #calculates to the  correlation coefficient between a specific factor and the average of prices
	test_map[columns[i]]=correlation; #Stores the vale along with factor name in a hash map


sorted_by_value = sorted(test_map.items(), key=lambda kv: kv[1]); #Sorteds the hash map by value;

for key,value in sorted_by_value: # prints test_map out
	if(value>=.5 or value<= -0.5):
		print(key,value);

print("\n");

test_map={};
for i in range(len(columns)):
	test_array=df[columns[i]]; #Finds the values for the specified factor
	correlation=np.corrcoef(test_array,array[:,1])[1,0]; #calculates to the  correlation coefficient between a specific factor and the average of prices
	test_map[columns[i]]=correlation; #Stores the vale along with factor name in a hash map


sorted_by_value = sorted(test_map.items(), key=lambda kv: kv[1]); #Sorteds the hash map by value;

for key,value in sorted_by_value: # prints test_map out
	if(value>=.5 or value<= -0.5):
		print(key,value);

#print(pca.explained_variance_ratio_);


test_map={};
for i in range(len(columns)):
	test_array=df[columns[i]]; #Finds the values for the specified factor
	correlation=np.corrcoef(test_array,array[:,2])[1,0]; #calculates to the  correlation coefficient between a specific factor and the average of prices
	test_map[columns[i]]=correlation; #Stores the vale along with factor name in a hash map


sorted_by_value = sorted(test_map.items(), key=lambda kv: kv[1]); #Sorteds the hash map by value;
print();
for key,value in sorted_by_value: # prints test_map out
	if(value>=.5 or value<= -0.5):
		print(key,value);

#print(pca.explained_variance_ratio_);
