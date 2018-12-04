import quandl
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
plt.style.use('ggplot')

from sklearn.linear_model import LinearRegression
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
quandl.ApiConfig.api_key = "dexFh9F13zbczB-4KeBo"

Stock = input("Entert TICKER of stock to predict: ")

df = quandl.get('WIKI/'+str(Stock))
print(df)

df = df[['Adj. Close', 'Adj. Volume']]
length = 30 



forecast_out = int(120)
df['Prediction'] = df[['Adj. Close']].shift(-forecast_out)
print(df)

X = np.array(df.drop(['Prediction'], 1))
X = preprocessing.scale(X)
print(X)

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


forecast_prediction = clf.predict(X_forecast)


df.dropna(inplace=True)
df['forecast'] = np.nan

last_date = df.iloc[-1].name
last_unix = last_date.timestamp() #last date in secounds 
one_day = 86400 #number of se in a day 
next_unix = last_unix + one_day #next day in unix 




for i in forecast_prediction:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    datetime.datetime.fromtimestamp(next_unix)
    next_unix += 86400
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)]+[i]
 

df['Adj. Close'].plot(figsize=(15,6), color="green")
df['forecast'].plot(figsize=(15,6), color="orange")
plt.xlim(xmin=datetime.date(2012, 5, 26),xmax=datetime.date(2019, 1, 1))
plt.title('SALES FORCE')
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()


