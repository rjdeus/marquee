import requests
import json
from ticker import ticker
from gsid import gsid

def main(gsidval):
    #gsidval = "11308"
    ticker_url = "https://api.marquee.gs.com/v1/assets/data/query"
    gsid_url = "https://api.marquee.gs.com/v1/data/USCANFPP_MINI/query"
    company_id = ticker(gsidval, ticker_url) # company_id = [company, gsid, ticker]
    #data = gsid(gsidval, gsid_url) # data = [growthScore, financialReturnsScore, multipleScore, integratedScore ]
    gsid_dataframe = gsid(gsidval, gsid_url) # dataframe with gsid data (4 things, + date)
    #print(company_id, stprice)
    #print(gsid_dataframe)
    return company_id, gsid_dataframe   
main("11308")

