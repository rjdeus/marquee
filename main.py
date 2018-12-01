import requests
import json
from ticker import ticker
from gsid import gsid

def main():
    gsidval = "11308"
    ticker_url = "https://api.marquee.gs.com/v1/assets/data/query"
    gsid_url = "https://api.marquee.gs.com/v1/data/USCANFPP_MINI/query"
    company_id = ticker(gsidval, ticker_url) # company_id = [company, gsid, ticker]
    #data = gsid(gsidval, gsid_url) # data = [growthScore, financialReturnsScore, multipleScore, integratedScore ]
    gsid_dataframe = gsid(gsidval, gsid_url) # datafram with gsid data (4 things, + date)
    print(gsid_dataframe)
    print(company_id)
main()    
