import http
import json

class CurrencyHelper:
	def __init__(self):

		self.client = http.client.HTTPSConnection('v2.ethereumprice.org', 8080)
		self.defaultHeaders = {"Content-type": "application/x-www-form-urlencoded"}
		self.payload = ''
		self.prices  = ''

		pass

	def makeRequest(self, url):

		self.client.request('GET', url + self.payload , '' , self.defaultHeaders)

		response = self.client.getresponse().read().decode('utf-8')

		self.prices = json.loads(response)

		self.client.close()

		return self.prices		

	def getBtcPrice(self):

		url = '/snapshot/btc/usd/waex/24h'
		return self.makeRequest(url)

	def getEthPrice(self):

		url = '/snapshot/eth/usd/waex/24h'
		return self.makeRequest(url)

	def getPrices(self):

		btc = self.getBtcPrice()
		eth = self.getEthPrice()

		return {'bitcoin': btc, 'ethereum': eth}

