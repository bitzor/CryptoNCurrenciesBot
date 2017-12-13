import http
import json

class CurrencyHelper:
	def __init__(self):

		self.client = http.client.HTTPSConnection('v2.ethereumprice.org', 8080)
		self.defaultHeaders = {"Content-type": "application/x-www-form-urlencoded"}
		self.payload = ''
		self.prices  = ''

		pass

	def getBtcPrice(self):

		result = self.client.request('GET', '/snapshot/btc/usd/waex/24h' + self.payload , '' , self.defaultHeaders)
		
		response 	  = self.client.getresponse().read().decode('utf-8')
		
		self.client.close()

		self.prices   = json.loads(response)

		return self.prices

	def getEthPrice(self):

		self.client.request('GET', '/snapshot/eth/usd/waex/24h', self.payload , self.defaultHeaders)
		
		response 	  = self.client.getresponse().read().decode('utf-8')

		self.client.close()
		
		self.prices   = json.loads(response)

		return self.prices		

	def getPrices(self):

		btc = self.getBtcPrice()
		eth = self.getEthPrice()

		return {'bitcoin': btc, 'ethereum': eth}