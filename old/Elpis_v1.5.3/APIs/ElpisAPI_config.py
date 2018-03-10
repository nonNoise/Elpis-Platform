# -*- coding: utf-8 -*-

##======================================##
## Configuration Block					##
##======================================##
class Conf:
	def __init__(self):
	## >>-------------------------------<< ##
		self.data = {
			"hello":"World",
			"day":"",
			"time":"",
			"ipaddr":"",
		}
	## >>-------------------------------<< ##
		self.HW_API = {
			"service_name":"",
			"hw_did":"",
			"state" :"",
			"SW1":"",
			"SW2":"",
			"SW3":"",
			"SW4":"",
			"SW5":"",
			"SW6":"",
			"wdog":"",
			
		}

		self.WEB_API = {
			"hw_did":"",
			"service_name":"",
			"api_ver":"",
			"state" :"",
			"state" :"",
			"SW1":"",
			"SW2":"",
			"SW3":"",
			"SW4":"",
			"SW5":"",
			"SW6":"",
			"wdog":"",
		}
