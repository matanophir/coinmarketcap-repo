import json
import requests
import pdb

url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '7a67af9d-a4b9-4bcc-b483-c7b9011f5a7b',
}
currency="ILS"
parameters = {
"start":"1",
"limit":"10",
"convert":currency,
"sort":"percent_change_24h"
}

request = requests.Session()
request.headers.update(headers)

results = request.get(url,params=parameters).json()
#print(json.dumps(results,sort_keys=True,indent=4))
#pdb.set_trace()
data= results["data"]
for curr in data:
	idn= curr["id"]
	sym= curr["symbol"]
	name= curr["name"]
	price= curr["quote"]["ILS"]["price"]
	change=curr["quote"]["ILS"]["percent_change_24h"]
	print (f"{idn} {sym} '{name}': \tprice- {price} \t 24 change- {change}")
