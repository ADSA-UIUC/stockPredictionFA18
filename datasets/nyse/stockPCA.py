import numpy as np;
import pandas as pd;
from sklearn.decomposition import PCA;
from sklearn.preprocessing import StandardScaler
import pylab
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

df=pd.read_csv("OP_NYSE.csv"); #Removes all non numeric columns from the data frame after importing the data
ticker_symbols = df.loc[:,['Ticker Symbol']].values #dataframe of just ticker symbols
df=df.loc[:, df.columns != 'Unnamed: 0.1'];
df=df.loc[:, df.columns != 'Ticker Symbol'];
df=df.loc[:, df.columns != 'Period Ending'];
df=df.loc[:, df.columns != 'GICS Sector'];
df=df.loc[:, df.columns != 'GICS Sub Industry'];

#df = df.dropna(axis='rows')
print(df.mean().head())
df.fillna(df.mean(), inplace=True) #fills missing values with averages
columns=df.columns #

x = StandardScaler().fit_transform(df); #standardizes data

pca=PCA(n_components=3) 
array=pca.fit_transform(df)
print('Variance: ' + str(sum(pca.explained_variance_ratio_)))
print(str(pca.n_components_) +' principal components with values of ' +str(pca.explained_variance_ratio_))

#plotting pc1 v pc2 v pc3
pcDF = pd.DataFrame(data = array[:,:3], columns = ['pc1','pc2','pc3']) #df of pc values for each non null training set, np.shape(pcDF) = (1016,2)
fig = plt.figure(figsize = (8,8))
ax3d = Axes3D(fig)
ax3d.set_xlabel('Principal Component 1', fontsize = 15)
ax3d.set_ylabel('Principal Component 2', fontsize = 15)
ax3d.set_title('3 Component PCA', fontsize = 20)
ax3d.scatter(pcDF['pc1'],pcDF['pc2'], pcDF['pc3'])
ax3d.grid()
pylab.show()

#plotting pc1 v pc2
pcDF = pd.DataFrame(data = array[:,:2], columns = ['pc1','pc2']) #df of pc values for each non null training set, np.shape(pcDF) = (1016,2)
fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 Component PCA', fontsize = 20)
ax.scatter(pcDF['pc1'],pcDF['pc2'])

ax.grid()
pylab.show()
