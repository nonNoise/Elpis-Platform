# -*- coding: utf-8 -*-
#client.py
import socket
import time
import json
import random
import uuid
import requests
from math import *

def Elpis_UDP_Client(host,port,data,sleeptime=1.0):
    time.sleep(sleeptime)
    clientsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    msg = json.dumps(data)
    print ("== Send ==")
    print ("host=%s , port=%d" % (host,port))
    print msg
    clientsock.sendto(msg, (host, port))
    print ("== Recv ==")
    rdata = clientsock.recv(1024)
    print rdata
    print ("== End. ==")
    clientsock.close()
    return rdata

#def Elpis_HTTP_Client(host,port,data,sleeptime=1.0):

#==================================================#
if __name__ == "__main__":

    cnt = 0
    data = {}
    data['devid'] = "TEST001" 
    data['time'] = "" 
    data['data'] = "" 
    data['temp'] = "" 
    data['hum'] = "" 
    data['cnt'] = 0
    
    a = 100     #振幅
    fs = 1000 #サンプリング周波数
    f0 = 10  #周波数
    sec = 1   #秒

    url = "http://127.0.0.1:5000/api/hw"

    

    import datetime
    while 1:
        for n in range(fs * sec):
            now = datetime.datetime.now()
            s = a * sin(2.0 * pi * f0 * n / fs)
            s2 = a * sin((2.0 * pi * f0 * n / fs)-20)
            print int(s)
            data['temp'] = "%d" % s 
            data['hum'] = "%d" % s2
            data['time'] = now.strftime("%H:%M:%S")
            data['data'] = now.strftime("%Y/%m/%d")
            data['cnt'] = cnt
            print json.dumps(data)
            cnt = cnt+1

           
            r = requests.post(url,data=json.dumps(data))
            print r.text
            time.sleep(1)
        