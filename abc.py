#!/usr/bin/python3
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
deviceId = "DUMzGTzh"
deviceKey = "Z9GFvxxp147vah0I" 
def post_to_mcs(payload): 
	headers = {"Content-type": "application/json", "deviceKey": deviceKey} 
	not_connected = 1 
	while (not_connected):
		try:
			conn = http.HTTPConnection("api.mediatek.com:80")
			conn.connect()
			not_connected = 0 
		except (http.HTTPException, socket.error) as ex: 
			print ("Error: %s" % ex)
			time.sleep(10)
	conn.request("POST", "/mcs/v2/devices/" + deviceId + "/datapoints", json.dumps(payload), headers) 
	response = conn.getresponse() 
	print( response.status, response.reason, json.dumps(payload), time.strftime("%c")) 
	data = response.read() 
	conn.close()
while True:
	SwitchStatus = GPIO.input(24)
	if(SwitchStatus == 0):
		print('Button pressed')
		payload={"datapoints":[{"dataChnId":"Switch","values":{"value":SwitchStatus}}]}
		time.sleep(5)
	else:
		print('Button released')
		payload={"datapoints":[{"dataChnId":"Switch","values":{"value":SwitchStatus}}]}
		time.sleep(5)
