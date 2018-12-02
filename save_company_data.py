from main import main
from pricetest import historicalPrice
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# call specific company gsid

def save():

    df = pd.read_csv('linked.csv')
    aggregate = []
    for i in df.values:
        company = []
        a = i.tolist()
        company.append(str(a[0]))               ## GSID
        company.append(str(a[1].strip()))       ## NAME
        company.append(str(a[2].strip()))       ## TICKER
        aggregate.append(company) 

    for i in range(len(aggregate)):
        myGSID = aggregate[i][0]
        print(myGSID)
        print(aggregate[i][2])
        company_id, gsid_df = main(myGSID)
        price_df = historicalPrice(aggregate[i][2], gsid_df['date'].iloc[0],gsid_df['date'].iloc[-1])
        merged = price_df.join(gsid_df)
        merged.to_csv("data/"+myGSID+".csv", encoding='utf-8', index=False)
save()
