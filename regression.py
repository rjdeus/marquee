import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

dataset = pd.read_csv('data/10516.csv')
print(dataset.shape)

'''
#for multiple regression model
X = dataset[['growthScore','financialReturnsScore','multipleScore','integratedScore']]
y = dataset['close']
'''

dataset['date']=pd.to_datetime(dataset['date'])
dataset['date']=dataset['date'].map(dt.datetime.toordinal)

#X=dataset[['growthScore']].values
X=dataset[['date']]
y=np.asarray(dataset['close'])

#80/20 split for training and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(X_train)
print('\n')
print(y_train)

#training algorithm
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

'''
#coefficient for multiple regression
coeff_df = pd.DataFrame(regressor.coef_, X.columns, columns=['Coefficient'])
print('\n')
print(coeff_df)
'''


#making predictions
y_pred = regressor.predict(X_test)
df = pd.DataFrame({'Actual' : y_test, 'Predicted' : y_pred})
#df.to_csv('regressionmodel.csv',encoding='utf-8',index=False)
#df.sort_index(inplace=True)
print('\n')
print('\n')
print(df)

#evaluating performance of algorithm
from sklearn import metrics
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))


print('\n')
plt.scatter(X_test, y_pred,  color='black')
plt.show()
