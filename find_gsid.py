import requests
import json
import pandas as pd

##comment

auth_data = {
    "grant_type"    : "client_credentials",
    "client_id"     : "d8cb805d98034326a3ffafd188992ad7",
    "client_secret" : "2b31959770d83c0fc381fc7c7444d561d5ed45c3739e38f412b92e645f35b799",
    "scope"         : "read_product_data"
}

# create session instance
session = requests.Session()

auth_request = session.post("https://idfs.gs.com/as/token.oauth2", data = auth_data)
access_token_dict = json.loads(auth_request.text)
access_token = access_token_dict["access_token"]

# update session headers with access token
session.headers.update({"Authorization":"Bearer "+ access_token})

request_url = "https://api.marquee.gs.com/v1/data/USCANFPP_MINI/query"


request_query = {
                   "startDate": "2005-01-01",
                   "endDate": "2018-12-31"
               }

request = session.post(url=request_url, json=request_query)
results = json.loads(request.text)

todf = results['data']

gsidList = []
tickerList = []
for i in range(len(todf)):
    if (todf[i]['gsid'] not in gsidList):
        gsidList.append(todf[i]['gsid'])

df = pd.DataFrame({'gsid':gsidList})
df.to_csv("data/gsid.csv", encoding = 'utf-8', index=False)
'''
outfile = open("data/gsid.txt", 'w')
outfile.write(df.to_string())
outfile.close()
'''

#with open('gsid.txt', 'w') as outfile
   # json.dump(results, outfile)
