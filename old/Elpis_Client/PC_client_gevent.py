#client.py
from gevent import monkey;monkey.patch_all()
import gevent

import socket
import time
import json
import random
import uuid

def client(cnt):
	#host = '133.242.190.76'
	host = '127.0.0.1'
	port = 16976

	#time.sleep(random.uniform(0.0001,1))
	time.sleep(0.5)
	clientsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	data = {}
	data['uuid'] = "3CD92B7A2447" #random.randint(1000,100000)#1234
	data['dvid'] = 1121#random.randint(1000,100000)#1234
	data['device'] = "Arduino_API"
	data['devip'] = ""
	data['devmac'] = ""
	data['elip'] = host
	data['elport'] = port
	data['acstime'] = ""
	data['ver'] = "1.0"	
	data['wdog'] = cnt

	data['ad1'] = cnt
	data['ad2'] = cnt
	data['ad3'] = cnt
	data['ad4'] = cnt


	#cnt = cnt+1
	msg = json.dumps(data)
	print msg
	clientsock.sendto(msg, (host, port))
	print clientsock.recv(1024)
	clientsock.close()



#==================================================#
if __name__ == "__main__":

	cnt = 0
#	for cnt in range(0,1000):
#		gevent.joinall([gevent.spawn(client,cnt) for i in xrange(0,1)])
	data = {}
	while 1 :
		host = '133.242.190.76'
		#host = '127.0.0.1'
		port = 16976

		#time.sleep(random.uniform(0.0001,1))
		time.sleep(1)
		clientsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		data['uuid'] = "3CD92B7A2447" #random.randint(1000,100000)#1234
		data['dvid'] = 1121#random.randint(1000,100000)#1234
		data['device'] = "Arduino_API"
		data['devip'] = ""
		data['devmac'] = ""
		data['elip'] = ""#host
		data['elport'] = ""#port
		data['acstime'] = ""	
		data['ver'] = "1.0"	
		data['wdog'] = cnt
		
		data['ad1'] = random.randint(1,100)

		data['ad2'] = random.randint(1,100)

		data['ad3'] = random.randint(1,100)

		data['ad4'] = random.randint(1,100)

		cnt = cnt + 1

		#cnt = cnt+1
		msg = json.dumps(data)
		print "SEND :"
		print msg
		clientsock.sendto(msg, (host, port))
		data =  json.loads(clientsock.recv(1024))		
		clientsock.close()
		print "RECIVE :"
		print data
