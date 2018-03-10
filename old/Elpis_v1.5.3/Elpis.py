# -*- coding: utf-8 -*-
#########################################################
#	 name 		: 	Elpis Framework					#####
#	 version	:	v1.5							#####
#	 programmer	:	Yuta Kitagami 					#####
#	 powerd		:	ArtifactNoise.com				#####
#	 farst		:	2014/09/28						#####
#	 next		:									#####
#########################################################
import json  
import datetime
import time
import os
import sys
import subprocess 
import argparse
from flask.ext.cors import CORS, cross_origin

from flask import Flask, make_response,request,abort, redirect, url_for, make_response
app = Flask(__name__)
cors = CORS(app)

#=================================================#
# Flask setting
#=================================================#
from APIs import root
app.register_module(root.app, url_prefix="/")
from APIs import document
app.register_module(document.app, url_prefix="/api")
from APIs import ElpisAPI
app.register_module(ElpisAPI.app, url_prefix="/api/")

#=================================================#
# Command parser
#=================================================#
parser = argparse.ArgumentParser(description='=== Elpis Framework ===')
parser.add_argument('--host', action="store", dest="host")
parser.add_argument('--port', action="store", dest="port",type=int)
parser.add_argument('--autodoc', action="store_true", dest="autodoc", default=False)
parser.add_argument('--debug', action="store_true", dest="debug",default=False)

command = parser.parse_args()

#=================================================#
# Main process
#=================================================#
if __name__ == '__main__':

	_htmlfile_ = "document.html"
	pypath = os.path.abspath(os.path.dirname(__file__))

	if command.autodoc == True:
		#subpro = subprocess.Popen(["python",pypath+"/APIs/docapi/main.py",pypath+"/APIs/docapi/nature.css",pypath+"/index.rst",pypath+"/templates/"+_htmlfile_ ])	
		subpro = subprocess.Popen(["python",pypath+"/doc/python/main.py"])	
	if command.debug == True:
		app.debug = True
	if command.host == None or command.host == "localhost":
		command.host = "127.0.0.1"
	print "=== Run ==="	
	app.run(host=command.host,port=command.port)
	if command.autodoc == True:
		subpro.kill()
	print ""
	print "Good by."




####################################################


