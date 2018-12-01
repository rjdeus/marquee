from datetime import datetime
from iexfinance.stocks import get_historical_data


start = '2015-05-01'
end = '2017-01-01'


df = get_historical_data("KO", start, end, output_format='pandas')
df = df.drop('open', axis=1)
df = df.drop('high', axis=1)
df = df.drop('low', axis=1)

print(df)