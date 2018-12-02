import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from regressiongSID import regress
from sklearn.model_selection import train_test_split
from sklearn import preprocessing, svm
from sklearn.linear_model import LinearRegression

myfile = 'data/10696.csv'
dataset = pd.read_csv(myfile)

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

### Join with Dates, output to graph, graphing actual to predicted prices

add_dates = df.join(dataset['date'])

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
#print(len(add_dates['date']))
lastdate = pd.to_datetime(dataset['date'].iloc[-1]).toordinal()
findate = pd.to_datetime('2018-06-05').toordinal()
Xnew=[i for i in range(lastdate+1,findate+1)]
Xneww = []
for i in Xnew:
    Xneww.append(dt.datetime.fromordinal(i).strftime("%Y-%m-%d"))
#print (pd.DataFrame({'date': Xneww}))


print("Predictive Model")

_, gS_new = regress('growthScore',myfile)
_, mS_new = regress('multipleScore',myfile)
_, iS_new = regress('integratedScore',myfile)
_, fRS_new = regress('financialReturnsScore',myfile)
x_future = [gS_new, mS_new, iS_new, fRS_new]
x_future_df = pd.DataFrame({'gS_New':gS_new['growthScore'], 'mS_New':mS_new['multipleScore'], 'iS_New':iS_new['integratedScore'],'fRS_New': fRS_new['financialReturnsScore']})
#print("x_future_df")
#print(x_future_df)
y_future = regressor.predict(x_future_df)

#print("np_asarray of add_dates['Predicted']")
#print(np.asarray(add_dates['Predicted']))

#print("y_future")
#print(y_future)
y_future_df = pd.DataFrame({'Predicted Values':y_future})
## added future values
concat = np.concatenate((np.asarray(add_dates['Predicted']), y_future), axis=None)
#print(concat)
#print(len(concat))
concat_df = pd.DataFrame({'Predicted':concat})
## added future dates
DATES = np.concatenate((np.asarray(add_dates['date']), Xneww), axis = None)
#print(len(add_dates['date']))
#print(type(add_dates['Actual']))

#print (concat_df.join(add_dates['Actual']).join(pd.DataFrame({'date':DATES})))
#toPrint = concat_df.join(add_dates['Actual']).join(pd.DataFrame({'date':DATES}))
toPrint = concat_df.join(pd.DataFrame({'date':DATES}))
toPrint.sort_values(by='date', ascending = True)

new_df = pd.merge(toPrint, add_dates, how='outer', on=['Predicted','date'])
print(new_df)

new_df.head(n=130).plot(x = 'date', y = ['Actual','Predicted'])
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
