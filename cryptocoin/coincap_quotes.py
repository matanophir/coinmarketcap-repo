import json
import requests
import pdb

class quote():
	"""one crypto curr information as an object"""
	url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
	headers = {
	'Accepts': 'application/json',
	'X-CMC_PRO_API_KEY': '7a67af9d-a4b9-4bcc-b483-c7b9011f5a7b',
	}
	def __init__(self, symbol,currency='ILS'):
		self.symbol = symbol
		self.currency=currency
		parameters = {
		'symbol':self.symbol,
		'convert':self.currency
		}
		request = requests.Session()
		request.headers.update(quote.headers)
		results = request.get(quote.url,params=parameters).json()
		data= results["data"]
		self.name=data[symbol]['name']
		self.id=data[symbol]['id']
		self.price=data[symbol]['quote'][self.currency]['price']
		self.last_update=data[symbol]["last_updated"]
		self.change1h=data[symbol]['quote'][self.currency]['percent_change_1h']
		self.change24h=data[symbol]['quote'][self.currency]['percent_change_24h']
		self.change7d=data[symbol]['quote'][self.currency]['percent_change_7d']

		




