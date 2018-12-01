from iexfinance.stocks import Stock

def price(ticker): 
	company = Stock(str(ticker))
	price = company.get_price()

	return price 

