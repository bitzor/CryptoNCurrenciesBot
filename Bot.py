
from ApiWrapper import *
from threading import Timer

class Bot: 

	def __init__(self):
		self.wrapper = ApiWrapper()
		self.bot = Timer(2, self.listen)

	def start(self):
		self.bot.start()
		pass

	def listen(self):
		""" Thread to listen incoming updates """
		print('Listening updates...')
		self.wrapper.getUpdates()
		handler = Timer(1, self.listen)
		handler.start()