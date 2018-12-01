from datetime import datetime
from iexfinance.stocks import get_historical_data

def historicalPrice(sYear,sMonth,sDay,eYear,eMonth,eDay)
	start = datetime(sYear, sMonth, sDay)
	end = datetime(eYear, eMonth, eDay)


	df = get_historical_data("KO", start, end, output_format='pandas')
	df = df.drop('open', axis=1)
	df = df.drop('high', axis=1)
	df = df.drop('low', axis=1)
	
	return df 