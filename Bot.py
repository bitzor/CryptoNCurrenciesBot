from ApiWrapper import *
from threading import Timer

class Bot: 

	def __init__(self):
		self.wrapper = ApiWrapper()
		self.bot = Timer(2, self.listen)
		self.updates = []
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
			chat_id = update['message']['chat']['id']
			self.wrapper.sendResponse(chat_id, 'Answering back')
			pass
		else:
			self.lastUpdateId = update['update_id'] + 1
			print(self.lastUpdateId)
		pass