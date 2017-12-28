from ApiWrapper import *
from CurrencyHelper import *
from threading import Timer
from datetime import date, datetime

class Bot: 

	def __init__(self):
		self.bot 	 	  = Timer(1, self.listen)
		self.helper  	  = CurrencyHelper()
		self.wrapper 	  = ApiWrapper()
		self.updates 	  = []
		self.lastUpdateId = ''
		pass

	def start(self):
		print('Listening updates...')
		self.bot.start()
		pass

	def listen(self):
		''' Thread to listen incoming updates '''

		updates = self.wrapper.getUpdates(self.lastUpdateId)

		if(updates['message'] == 'OK'):
			self.updates = updates['updates']
			self.processUpdates()
		else: 
			print(updates['message'])

		handler = Timer(1, self.listen)
		handler.start()

		pass

	def processUpdates(self):
		for update in self.updates:
			name	= update['message']['from']['first_name'] 
			chat_id = update['message']['chat']['id']
			command = update['message']['text']

			command_response = self.processCommand(command)

			self.wrapper.sendResponse(chat_id, command_response)
			
			print('Incoming command from ' + name + ': '+ command)
		else:
			self.lastUpdateId = update['update_id'] + 1
		pass

	def processCommand(self, command):
		emoji = u'\U0001F4B9'
		dt = datetime.today().strftime('%A, %d/%m/%Y - %I:%M:%S %p')
		response = '*Price Summary* ' + emoji + '\n' + dt + ' \n\n'

		if (command == '/all'):
			response += self.processAllCommand()
		elif(command == '/bitcoin' or command == '/btc'):
			response += self.processBtcCommand()
		elif(command == '/ethereum' or command == '/eth'):
			response += self.processEthCommand()
		elif(command == '/help' or command == '/start'):
			response = self.helpCommand()
		else:
			response = '*No command available*'
		return response

	def processBtcCommand(self):

		price = self.helper.getBtcPrice()
		btc = repr(price['data']['price'])
		emoji = u'\U0001F4B8'
		return '*BTC*: ' + btc + ' USD' + emoji

	def processEthCommand(self):

		price = self.helper.getEthPrice()
		eth = repr(price['data']['price'])
		emoji = u'\U0001F539'
		return '*ETH*: ' + eth + ' USD' + emoji

	def processAllCommand(self):
		
		response = self.processBtcCommand()
		response += '\n' + self.processEthCommand()

		return response

	def helpCommand(self): 
		return '''
				*Welcome to CryptoCurrenciesBot!*

				- Use _/all_ command to query all Bitcoin and Ethereum Prices
				- Use _/bitcoin_ or _/btc_ to query Bitcoin price
				- Use _/ethereum_ or _/eth_ to query Ethereum price
			'''