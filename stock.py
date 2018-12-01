import quandl
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
quandl.ApiConfig.api_key = "mXy8Yh9rUmwPNmQvnUAj"

df = quandl.get("WIKI/AMZN")
df = df[['Adj. Close']]
length = 30 


forecast_out = int(30)
df['Prediction'] = df[['Adj. Close']].shift(-forecast_out)
print(df)


X = np.array(df.drop(['Prediction'], 1))
X = preprocessing.scale(X)

X_forecast = X[-forecast_out:] # set X_forecast equal to last 30
X = X[:-forecast_out] # remove last 30 from X

y = np.array(df['Prediction'])
y = y[:-forecast_out]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

# Training
clf = LinearRegression()
clf.fit(X_train,y_train)
# Testing
confidence = clf.score(X_test, y_test)
print("confidence: ", confidence)

realPricebuff = np.array(df.tail(length))
realPrice = []

for i in range(length):
	realPrice.append(realPricebuff[i][0])


forecast_prediction = clf.predict(X_forecast)



'''
print(forecast_prediction)
print(realPrice)




t= list(range(30))

plt.plot(t,forecast_prediction,'r')
plt.plot(t, realPrice, 'b')
plt.show()
'''
