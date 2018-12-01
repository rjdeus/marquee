import requests
import json

auth_data = {
    "grant_type"    : "client_credentials",
    "client_id"     : "d8cb805d98034326a3ffafd188992ad7",
    "client_secret" : "7614bae6b68c3ea0014fa05246c257616b9c00ac5b70dc8687ed066a5cf98c11",
    "scope"         : "read_product_data"
}

# create session instance
session = requests.Session()

auth_request = session.post("https://idfs.gs.com/as/token.oauth2", data = auth_data)
access_token_dict = json.loads(auth_request.text)
access_token = access_token_dict["access_token"]

# update session headers with access token
session.headers.update({"Authorization":"Bearer "+ access_token})

request_url = "https://api.marquee.gs.com/v1/assets/data/query"

request_query = {
                    "where": {
                        "gsid": ["901237"]
                    },
                    "fields":["gsid","ticker","name"]
               }

request = session.post(url=request_url, json=request_query)
results = json.loads(request.text)
print(results)
print("\n")
