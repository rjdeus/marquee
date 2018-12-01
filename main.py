import requests
import json
from ticker import ticker
from gsid import gsid
from price import price 

def main(gsidval):
    #gsidval = "11308"
    ticker_url = "https://api.marquee.gs.com/v1/assets/data/query"
    gsid_url = "https://api.marquee.gs.com/v1/data/USCANFPP_MINI/query"
    company_id = ticker(gsidval, ticker_url) # company_id = [company, gsid, ticker]
    #data = gsid(gsidval, gsid_url) # data = [growthScore, financialReturnsScore, multipleScore, integratedScore ]
    gsid_dataframe = gsid(gsidval, gsid_url) # datafram with gsid data (4 things, + date)
<<<<<<< HEAD
    stprice = price(company_id[2])
    company_id.append(stprice)
    print(company_id, stprice)
    print(gsid_dataframe)

main()    
=======
    #print(gsid_dataframe)
    #print(company_id)
    return company_id, gsid_dataframe    
main("11308")
>>>>>>> 58a0b5791b3b2dd36300f2de89b99894bbe233d5
