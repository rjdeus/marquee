from datetime import datetime
from iexfinance.stocks import get_historical_data


def historicalPrice(dStart, dEnd):
	df = get_historical_data("KO", dStart, dEnd, output_format='pandas')
	df = df.drop('open', axis=1)
	df = df.drop('high', axis=1)
	df = df.drop('low', axis=1)
	return df 

