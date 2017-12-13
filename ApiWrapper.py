import http.client
import json


class ApiWrapper:
	def __init__(self, botToken = '458287424:AAHI0-WT61_uM6um1JtDsKOl5_VyZVEORoo'):
		self.botToken 		= botToken
		self.defaultHeaders = {"Content-type": "application/json"}
		self.client 		= http.client.HTTPSConnection('api.telegram.org', 443)
		pass

	def getUpdates(self, lastUpdateId):
		updates = {}
		message = 'OK'
		payload = json.dumps({'offset': lastUpdateId})
		try:
			result   		= self.client.request('GET', '/bot'+ self.botToken + '/getUpdates', payload , self.defaultHeaders)
			response 		= self.client.getresponse()
			raw_body 		= response.read().decode('utf-8')
			json_response 	= json.loads(raw_body)

			if(json_response['ok'] and len(json_response['result']) > 0):
				updates = json_response['result']
			else:
				message = 'No updates available'
		except:
		    raise
		
		return {'updates': updates, 'message': message}

	def sendResponse(self, chatId, message):
		payload = json.dumps({'chat_id': chatId, 'text': message, 'parse_mode': 'MARKDOWN'})
		try:
			print("Sending response: " + message)
			print(payload)
			result   = self.client.request('POST', '/bot'+ self.botToken + '/sendMessage', payload , self.defaultHeaders)
			response = self.client.getresponse()
			body 	 = response.read()
			return body
		except:
		    raise
		pass		
