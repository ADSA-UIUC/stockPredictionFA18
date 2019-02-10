import pandas as pd
import quandl, math
import datetime as dt
import time
import numpy as np
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style
import pickle
style.use('ggplot')

df = pd.read_csv('GOOG.csv')
#print('size of data: '+str(np.shape(df)))
df = df[['Date','Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close'])/ df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open'])/ df['Adj. Open'] * 100.0

df = df[['Date','Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

forecast_col = 'Adj. Close' # variable to predict
df.fillna(-99999, inplace=True) #NaN entries will be treated as outliers

#math.ceil rounds up. This returns "about 1 percent of the dataset"
forecast_out = int(math.ceil(0.01*len(df))) 
#we are trying to predict one percent of dataframe(using feature data that came 1 day ago(if 100days) to predict today)
#shifts the Adj. Close prices to make the features correspond to the Adj. Close prices 1% days into the future
#this way we can predict, based on current features, what the closing price in 10 days will be
df['label'] = df[forecast_col].shift(-forecast_out) 


X = np.array(df.drop(['label','Date'],1)) #everything except output
X = preprocessing.scale(X) #scales X
X = X[:-forecast_out]
X_lately = X[-forecast_out:]

df.dropna(inplace=True) #drops rows with NaN values
y = np.array(df['label'])


#print(len(X),len(y)) #check if same lengths

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2) #20 percent of data used as testing data
#X_train and y_train are used to fit classifier
# clf = LinearRegression(n_jobs=-1)#n_jobs = -1. Run on as many threads as the processor can handle
# clf.fit(X_train, y_train)             #fit = 'train'
# with open('linearregression.pickle','wb') as f:
# 	pickle.dump(clf,f)

pickle_in = open('linearregression.pickle','rb') #get classifier
clf = pickle.load(pickle_in)       
accuracy = clf.score(X_test,y_test)   #score = 'test'
#print(accuracy)
forecast_set = clf.predict(X_lately)
#print(forecast_set, accuracy,forecast_out) #next thirty five days of prices

#adds a column 'Forecast' as nans
df['Forecast'] = np.nan
d = df['Date']

#plotting date
last_date = df.iloc[-1].Date
last_unix = time.mktime(dt.datetime.strptime(last_date, "%Y-%m-%d").timetuple())
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
	next_date = dt.datetime.fromtimestamp(next_unix)
	next_unix += one_day
	df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]

print(df.head())
df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

