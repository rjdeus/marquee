#import quandl
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
from datetime import datetime

plt.style.use('ggplot')

from sklearn.linear_model import LinearRegression
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
#quandl.ApiConfig.api_key = "mXy8Yh9rUmwPNmQvnUAj"

Stock = input("Entert GSID of stock to predict ")

df = pd.read_csv('data/'+str(Stock)+'.csv')
df = df[['close', 'volume','growthScore','multipleScore','integratedScore','financialReturnsScore','date']]
length = 30 

dateb = np.array(df[['date']])
Date=[]
for i in range(len(dateb)):
	Date.append(datetime.strptime(str(dateb[i][0]), '%Y-%m-%d'))

dateb= np.array(Date)
#print(dateb)
df['date']=dateb[:]


df2 = df.drop(['close', 'volume','growthScore','multipleScore','integratedScore','financialReturnsScore'],1)

#f3 = df.drop(['date'],1)


df3=df2.set_index('date').join(df.set_index('date'))
print(df3)

#df3=df2.drop(['close', 'volume','growthScore','multipleScore','integratedScore','financialReturnsScore'],1)
#df4=df3.set_index('date').join(df.set_index('date'))
#df3.set_index('date').join(df.set_index('date'))




forecast_out = int(30)
df['Prediction'] = df[['close']].shift(-forecast_out)


X = np.array(df.drop(['Prediction','date'], 1))
X = preprocessing.scale(X)
#print(X)

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
print("_______________________________________")


forecast_prediction = clf.predict(X_forecast)


df.dropna(inplace=True)
df['forecast'] = np.nan

last_date = df.iloc[-1].date 
last_unix = last_date.timestamp() #last date in secounds 
one_day = 86400 #number of se in a day 
next_unix = last_unix + one_day #next day in unix 
print(forecast_prediction)





for i in forecast_prediction:
    next_date = datetime.fromtimestamp(next_unix)
    next_unix += 86400
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)]+[i]
 

df['close'].plot(figsize=(15,6), color="green")
df['forecast'].plot(figsize=(15,6), color="orange")
plt.legend(loc=4)
plt.title('NETFLIX INC')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

