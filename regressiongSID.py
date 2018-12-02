import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

def regress(datatype,filename):
    dataset = pd.read_csv(filename)

#####
    lastdate = pd.to_datetime(dataset['date'].iloc[-1]).toordinal()
    findate = pd.to_datetime('2018-06-05').toordinal()


    dataset['date']=pd.to_datetime(dataset['date'])
    dataset['date']=dataset['date'].map(dt.datetime.toordinal)

    X=dataset[['date']]
    
    y=np.asarray(dataset[datatype])

    #80/20 split for training and test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    #training algorithm
    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    #making predictions
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
    #*******PREDICT FUTURE VALS*****
    Xnew=[i for i in range(lastdate+1,findate+1)]
    Xnewdf = pd.DataFrame({"Xnew":Xnew})
    ynew=regressor.predict(Xnewdf)
    ynewdf = pd.DataFrame({datatype:ynew})
    
    return df, ynewdf
