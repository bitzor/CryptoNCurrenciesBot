import http.client

class ApiWrapper:
	def __init__(self, botToken = '386677141:AAHmjcer9dLqwvFctWm6h9nBLmMXTxS3qyg'):
		self.botToken = botToken
		self.defaultHeaders = {"Content-type": "application/x-www-form-urlencoded"}
		self.client = http.client.HTTPSConnection('api.telegram.org', 443)

	def getUpdates(self):
		try:
			result = self.client.request('GET', '/bot'+ self.botToken + '/getUpdates', '' , self.defaultHeaders)
			response = self.client.getresponse()
			body = response.read()
			#command = body.result[0].message.text[1:]
			print(body)

		except:
		    raise
		
		pass