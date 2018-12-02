from datetime import datetime
from iexfinance.stocks import get_historical_data


def historicalPrice(ticker, dStart, dEnd):
	df = get_historical_data(ticker, dStart, dEnd, output_format='pandas')
	df = df.drop('open', axis=1)
	df = df.drop('high', axis=1)
	df = df.drop('low', axis=1)
	df.index = range(len(df))
	return df
