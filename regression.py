import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from regressiongSID import regress
from sklearn.model_selection import train_test_split
from sklearn import preprocessing, svm
from sklearn.linear_model import LinearRegression

myfile = 'data/10516.csv'
dataset = pd.read_csv(myfile)
#print(dataset.shape)
#print(dataset.head())
#print(dataset.describe())

X = dataset[['growthScore','multipleScore','integratedScore','financialReturnsScore']]
y = dataset['close']

#80/20 split for training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#training algorithm
regressor = LinearRegression()
regressor.fit(X_train, y_train)

coeff_df = pd.DataFrame(regressor.coef_, X.columns, columns=['Coefficient'])
print(coeff_df)

#making predictions
y_pred = regressor.predict(X_test)
df = pd.DataFrame({'Actual' : y_test, 'Predicted' : y_pred})
df.sort_index(inplace=True)

#print(df)

### Join with Dates, output to graph, graphing actual to predicted prices

add_dates = df.join(dataset['date'])
print(add_dates)

add_dates.plot(x = 'date', y = ['Actual','Predicted'])
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

#evaluating performance of algorithm
from sklearn import metrics
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

## Predictive Model

'''
plt.scatter(X_test, y_test,  color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
'''
print("Predictive Model")

_, gS_new = regress('growthScore',myfile)
_, mS_new = regress('multipleScore',myfile)
_, iS_new = regress('integratedScore',myfile)
_, fRS_new = regress('financialReturnsScore',myfile)
x_future = [gS_new, mS_new, iS_new, fRS_new]
for i in x_future:
    print(i)
x_future_df = pd.DataFrame({'gS_New':gS_new['growthScore'], 'mS_New':mS_new['multipleScore'], 'iS_New':iS_new['integratedScore'],'fRS_New': fRS_new['financialReturnsScore']})
print(x_future_df)
y_future = regressor.predict(x_future_df)
print(len(y_future))

