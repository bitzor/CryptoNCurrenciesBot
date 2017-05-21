import http.client

botToken = '386677141:AAHmjcer9dLqwvFctWm6h9nBLmMXTxS3qyg'
headers = {"Content-type": "application/x-www-form-urlencoded"}
client = http.client.HTTPSConnection('api.telegram.org', 443)
try:
	result = client.request('GET', '/bot'+ botToken + '/getUpdates', '' ,headers)
	response = client.getresponse()
	body = response.read()
	print(body)
except:
    raise