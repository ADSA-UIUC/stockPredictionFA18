import numpy as np
import pandas as pd
# Import data
data = pd.read_csv('datasets/nyse/prices.csv')
# Drop date variable
data = data.drop(['DATE'], 1)
# Dimensions of dataset
n = data.shape[0]
p = data.shape[1]
# Make data a numpy array
data = data.values