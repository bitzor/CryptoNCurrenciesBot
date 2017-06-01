from ApiWrapper import *
from Helper import *
from threading import Timer

class Bot: 

	def __init__(self):
		self.helper  	  = Helper()
		self.wrapper 	  = ApiWrapper()
		self.bot 	 	  = Timer(2, self.listen)
		self.updates 	  = []
		self.lastUpdateId = ''
		pass

	def start(self):
		self.bot.start()
		pass

	def listen(self):
		""" Thread to listen incoming updates """
		print('Listening updates...')
		
		response = self.wrapper.getUpdates(self.lastUpdateId)

		if(response['message'] == 'OK'):
			self.updates = response['updates']
			self.processUpdates()
		else: 
			print(response['message'])

		handler = Timer(1, self.listen)
		handler.start()

		pass

	def processUpdates(self):
		for update in self.updates:			
			name	=  update['message']['from']['first_name'] 
			chat_id = update['message']['chat']['id']
			command = update['message']['text']

			print("Incoming command from " + name + ': '+ command)

			response = self.processCommand(chat_id, command)
			print(response)
			print(type(response))
			self.wrapper.sendResponse(chat_id, response)

		else:
			self.lastUpdateId = update['update_id'] + 1
			print(self.lastUpdateId)
		pass

	def processCommand(self, chat_id, command):
		prices =  {}

		if(command == '/bitcoin'):
			prices = self.helper.getBtcPrice()
		elif(command == '/ethereum'):
			prices = self.helper.getEthPrice()
		elif(command == '/all'):
			prices = self.helper.getPrices()

		response = self.prepareResponse(prices, command)

		return response
		
	def prepareResponse(self, prices, command):
		text = ''

		if(command == '/bitcoin'):
			text = "*BTC*: " + prices['current_price']+ ' USD'
		elif(command == '/ethereum'):
			text = " *ETH*: " + prices['current_price']+ ' USD'
		elif(command == '/all'):
			text = " *BTC*: " + prices['bitcoin']['current_price']  + ' USD\n' + "*ETH*: " + prices['ethereum']['current_price'] + ' USD '
		elif(command == '/start'):
			text = """
				*Welcome to EthBitBot!*

				- Use _/all_ command to query all Bitcoin and Ethereum Prices
				- Use _/bitcoin_ to query Bitcoin price
				- Use _/ethereum_ to query Ethereum price
			"""

		return text