from main import main
from pricetest import historicalPrice
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# call specific company gsid

def save():

    df = pd.read_csv('data\linked.csv')
    #print(df)
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
        company_id, gsid_df = main(myGSID)
        price_df = historicalPrice(gsid_df['date'].iloc[0],gsid_df['date'].iloc[-1])
        merged = price_df.join(gsid_df)
        merged.to_csv("data/"+myGSID+".csv", encoding='utf-8', index=False)

    ###attributes = ['growthScore','financialReturnsScore','multipleScore','integratedScore']

    #### Tables
        
    '''
    plt.rcParams["figure.figsize"] = [plt.rcParams["figure.figsize"][0] *2, plt.rcParams["figure.figsize"][1]]
    merged.plot(x = 'date', y = attributes)
    plt.legend(bbox_to_anchor=(0.7, 0.7), loc=2,
               ncol=2, mode="expand", borderaxespad=0.)
    plt.suptitle(company_id[0] + ": Fundamental Attributes vs Time")
    plt.ylabel("Attribute Value")
    plt.xlabel("Date")
    #plt.savefig('attributetime.png')

    merged.plot(x = 'date', y = 'close')
    plt.title(company_id[0] + ": Close Price vs Time")
    leg = plt.legend( loc = 'best')
    plt.ylabel("Cost ($ US)")
    plt.xlabel("Date")
    #plt.savefig('costtime.png')
    plt.show()
    '''

    '''
    plt.plot(merged['date'], merged['growthScore'])
    plt.title(company_id[0] + " growthScore over Time")
    plt.xticks([merged['date'].iloc[0],merged['date'].iloc[len(merged['date'])//2],merged['date'].iloc[-1]])
    plt.show()
    '''
