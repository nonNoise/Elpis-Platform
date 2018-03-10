# -*- coding: utf-8 -*-
from flask import Module, render_template, make_response,url_for
app = Module(__name__)


#=====================================================================================#
# Document
#=====================================================================================#
@app.route("")
def document():
	#response = make_response(render_template('document.html'))
	response = make_response(render_template('document.html'))
	response.headers.add('Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')
	return response

