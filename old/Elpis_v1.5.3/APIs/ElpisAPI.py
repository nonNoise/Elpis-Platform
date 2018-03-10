# -*- coding: utf-8 -*-
from flask import Module, render_template, make_response,url_for,request, current_app
from datetime import timedelta  
from flask import Flask, make_response, request, current_app ,jsonify
from functools import update_wrapper
import os
import json

app = Module(__name__)

import ElpisAPI_config
Elpis = ElpisAPI_config.Conf()	

files = {}
doc = {}
files["root"] =  "/home/kitagami/Github/Elpis/ElpisHW/JSON"


#=====================================================================================#
# Web-API
#=====================================================================================#
@app.route("<service>/<uuid>", methods=['POST','GET'])
#@crossdomain(origin='*')
def webapi(service,uuid):
	jdata = {}
	data = {}
	#---------------------------------------------------------#
	# Init Data Loading
	#---------------------------------------------------------#
	#jdata["web_input"] = request.values["jdata"]
	#data =  json.loads(jdata["web_input"])
	#print "Get: ",		
	data["service"] = service #"SW_API"
	data["uuid"] = uuid
	print service
	print uuid
	#---------------------------------------------------------#
	# File Open and Setting
	#---------------------------------------------------------#
	files["jsondir"] =  files["root"] + "/"+service 
	doc["input"] = files["jsondir"]+"/"+data["uuid"]+"/"+data["uuid"]+"_Input.json"
	doc["output"] = files["jsondir"]+"/"+data["uuid"]+"/"+data["uuid"]+"_Output.json"
	print files["root"] 
	
	#---------------------------------------------------------#
	# Writting to POST request
	#---------------------------------------------------------#
	if request.method == 'POST':
		jdata["web_input"] = request.values["jdata"]
		data =  json.loads(jdata["web_input"])
		f = open(doc["output"] ,"w")
		json.dump(data, f,sort_keys=True) #, sort_keys=True, indent=4
		f.close()	
	
	#---------------------------------------------------------#
	# Return Data
	#---------------------------------------------------------#		
	try:
		f = open(doc["input"] ,"r")
		jdata["hw_input"] = json.load(f)
		f.close()	
	except IOError:
		print doc["input"] 
		print "Dont Open. IOError"
		jdata["hw_input"] = {}
		return "{status:\"404 Hardware Not Found.\"}"
	#print len(jdata["hw_input"])
	try:
		print "Put: ",		
		print  jdata["hw_input"][len(jdata["hw_input"])-1]
		return json.dumps(jdata["hw_input"][len(jdata["hw_input"])-1])
	except KeyError:
		print "KeyError"
		return "{status:\"503 Key ERROR\"}"
