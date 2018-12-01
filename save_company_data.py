from main import main
from pricetest import historicalPrice
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# call specific company gsid

myGSID = "11308"
company_id, gsid_df = main(myGSID)
# date range
price_df = historicalPrice(gsid_df['date'].iloc[0],gsid_df['date'].iloc[-1])

#gsid_dataframe.plot(kind='scatter',x='growthScore',y='multipleScore',color='red')
#plt.title(company_id[0])
#plt.show()

#gsid_df.plot(kind='scatter',y='growthScore',x='date', color='blue')
#plt.title(company_id[0] + "growthScore vs date")
#plt.show()

#print(list(price_df))
#print(list(gsid_df))

merged = price_df.join(gsid_df)

print(list(merged))

print(merged)
#print(merged.dtypes)
outfile = open("data/"+myGSID+".txt", 'a')
outfile.write(merged.to_string())
outfile.close()
attributes = ['growthScore','financialReturnsScore','multipleScore','integratedScore']
'''
plt.plot(merged['growthScore'])
plt.plot(merged['financialReturnsScore'])
plt.plot(merged['multipleScore'])
plt.plot(merged['integratedScore'])
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
plt.plot(merged['date'], merged['growthScore'])
plt.title(company_id[0] + " growthScore over Time")
plt.xticks([merged['date'].iloc[0],merged['date'].iloc[len(merged['date'])//2],merged['date'].iloc[-1]])
plt.show()
'''
