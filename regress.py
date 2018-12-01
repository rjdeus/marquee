from main import main
from pricetest import historicalPrice
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

company_id, gsid_df = main("11308")
#print(gsid_df)
#print("\n")
print(company_id)

price_df = historicalPrice(gsid_df['date'].iloc[0],gsid_df['date'].iloc[-1])

#gsid_dataframe.plot(kind='scatter',x='growthScore',y='multipleScore',color='red')
#plt.title(company_id[0])
#plt.show()
print(price_df)
print(gsid_df)

#gsid_df.plot(kind='scatter',y='growthScore',x='date', color='blue')
#plt.title(company_id[0] + "growthScore vs date")
#plt.show()

merged = pd.merge(price_df, gsid_df, on = ['date'])
print("merged")
print(merged)
