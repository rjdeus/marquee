import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

def regress(datatype,filename):
    dataset = pd.read_csv(filename)

    dataset['date']=pd.to_datetime(dataset['date'])
    dataset['date']=dataset['date'].map(dt.datetime.toordinal)

    X=dataset[['date']]
    #print(lastday=X[-1])
    
    y=np.asarray(dataset[datatype])

    #80/20 split for training and test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    #training algorithm
    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    #making predictions
    print('X_test')
    #print(type(X_test))
    print(X_test)
    y_pred = regressor.predict(X_test)
    df = pd.DataFrame({'Actual' : y_test, 'Predicted' : y_pred})
    #print('df')
    #print(df)

    '''
    print(X_test)
    print(y_pred)
    dates_new=pd.to_datetime(y_pred)
    dates_new=y_pred.map(dt.datetime.toordinal)
    '''

    ##plt.scatter(X_test['date'],df['Actual'])
    ##plt.scatter(X_test['date'],df['Predicted'])
    ##plt.show()

    '''
    length=len(df.index)
    print(length)
    '''
    #*******PREDICT FUTURE VALS*****
    '''
    Xnew = [[51236]]
    ynew=regressor.predict(Xnew)
    print(ynew)
    '''
    lastdate = pd.to_datetime(dataset['date'].iloc[-1]).toordinal()
    findate = pd.to_datetime('2018-06-05').toordinal()
    Xnew=[i for i in range(lastdate,findate)]
    Xnewdf = pd.DataFrame({"Xnew":Xnew})
    
    print('Xnewdf')
    print(Xnewdf)
    print(type(Xnewdf))
    ynew=regressor.predict(Xnewdf)
    ynewdf = pd.DataFrame({datatype:ynew})
    
    return df, ynewdf
