from main import main
from pricetest import historicalPrice
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

company_id, gsid_dataframe = main("11308")
print(gsid_dataframe)
print("\n")
print(company_id)

price_datafrane = historicalPrice()

#gsid_dataframe.plot(kind='scatter',x='growthScore',y='multipleScore',color='red')
#plt.title(company_id[0])
#plt.show()

gsid_dataframe.plot(kind='scatter',y='growthScore',x='date', color='blue')
plt.title(company_id[0] + "growthScore vs date")
plt.show()
