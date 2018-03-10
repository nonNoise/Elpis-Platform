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
@app.route("", methods=['POST','GET'])
def webos():
	items = {}
	items.update( {"active":"home"})
	items.update ({"other":("1","2","3")})
	print items
	response = make_response(render_template('control.html', items = items))
	response.headers.add('Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')
	#response.cache_control.no_cache = False
	return response


@app.route("<service>/<uuid>", methods=['POST','GET'])
def apiapi(service,uuid):
	return "OK"

