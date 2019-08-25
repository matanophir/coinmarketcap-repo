import json
import requests

url = 'https://sandbox-api.coinmarketcap.com/v1/global-metrics/quotes/latest'

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '7a67af9d-a4b9-4bcc-b483-c7b9011f5a7b',
}
currency="ILS"
parameters = {
  'convert':currency
}

request = requests.Session()
request.headers.update(headers)
results = request.get(url,params=parameters).json()

#print(json.dumps(results,sort_keys=True,indent=4))

active_cryptocurrencies=results["data"]["active_cryptocurrencies"]

active_market_pairs=results["data"]["active_market_pairs"]
active_exchanges=results["data"]["active_exchanges"]
eth_dominance=results["data"]["eth_dominance"]
btc_dominance=results["data"]["btc_dominance"]
total_market_cap=results["data"]["quote"][currency]["total_market_cap"]
total_volume_24h=results["data"]["quote"][currency]["total_volume_24h"]
last_updated=results["data"]["last_updated"]
print(f"active market pairs: {active_market_pairs}")
print(f"active exchange: {active_exchanges}")
print(f"btc dominance: {btc_dominance}")
print(f"total market cap in ILS: {total_market_cap}%")
up=str(last_updated).split("T")
print(f"last updated: {up[0]}")



