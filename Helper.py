import http
import json

class Helper:
	def __init__(self):

		self.client = http.client.HTTPSConnection('ethereumprice.org', 443)
		self.defaultHeaders = {"Content-type": "application/x-www-form-urlencoded"}
		self.payload = ''
		self.prices  = ''

		pass

	def getBtcPrice(self):

		self.payload  = 'coin=btc&cur=btcusd&ex=waex&dec=2'

		print(self.payload)

		self.client.request('GET', '/wp-content/themes/theme/inc/exchanges/price-data.php', self.payload , self.defaultHeaders)
		
		response 	  = self.client.getresponse().read().decode('utf-8')
		
		self.prices   = json.loads(response)

		return self.prices

	def getEthPrice(self):

		self.payload  = 'coin=eth&cur=ethusd&ex=waex&dec=2'
		
		self.client.request('GET', '/wp-content/themes/theme/inc/exchanges/price-data.php', self.payload , self.defaultHeaders)
		
		response 	  = self.client.getresponse().read().decode('utf-8')

		self.prices   = json.loads(response)

		return self.prices		

	def getPrices(self):

		btc = self.getBtcPrice()
		eth = self.getEthPrice()

		return {'bitcoin': btc, 'ethereum': eth}