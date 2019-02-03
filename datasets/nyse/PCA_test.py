import numpy as np;
import pandas as pd;
from sklearn.decomposition import PCA;
from sklearn.preprocessing import StandardScaler



df=pd.read_csv("OP_NYSE.csv"); #Removes all non numeric columns from the data frame after importing the data
df=df.loc[:, df.columns != 'Unnamed: 0.1'];
df=df.loc[:, df.columns != 'Ticker Symbol'];
df=df.loc[:, df.columns != 'Period Ending'];
df=df.loc[:, df.columns != 'GICS Sector'];
df=df.loc[:, df.columns != 'GICS Sub Industry'];

df=df.dropna(axis='rows'); #drops all rows without full aet of data may need to revise in the future.

columns=df.columns #

x = StandardScaler().fit_transform(df); #standardizes data







pca=PCA(n_components=30); #uses 3 components

array=pca.fit_transform(df); #Finds the values along each dimension


def print_axis_correlations(df,array,index):
	test_map={};
	for i in range(len(columns)):
		test_array=df[columns[i]]; #Finds the values for the specified factor
		correlation=np.corrcoef(test_array,array[:,index])[1,0]; #calculates to the  correlation coefficient between a specific factor and component axis
		test_map[columns[i]]=correlation; #Stores the vale along with factor name in a hash map


	sorted_by_value = sorted(test_map.items(), key=lambda kv: kv[1]); #Sorted the hash map by value;

	for key,value in sorted_by_value: # prints test_map out
		if(value>=.3 or value<= -0.3):
			print(key,value);
	print("\n");


for i in range(30): #prints for each component axis
	print("Principal Component Axis:",str(i));
	print_axis_correlations(df,array,i);

