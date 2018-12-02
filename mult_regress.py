import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import preprocessing, svm
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('data/10516.csv')
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
print(df)
df.sort_index(inplace=True)
print(df)


#evaluating performance of algorithm
from sklearn import metrics
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

'''
plt.scatter(X_test, y_test,  color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
'''
