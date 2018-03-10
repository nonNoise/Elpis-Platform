# -*- coding: utf-8 -*-
from flask import Module, render_template, make_response,url_for,Blueprint
DOC_URL = "../doc/_build/html/"
STATIC_URL =  "_static"
IMAGES_URL = "_images"

doc = Blueprint('document', __name__,template_folder=DOC_URL)
doc_static = Blueprint('sphinx_static', __name__,static_folder=DOC_URL +STATIC_URL,static_url_path=STATIC_URL)
doc_images = Blueprint('sphinx_images', __name__,static_folder=DOC_URL +IMAGES_URL,static_url_path=IMAGES_URL)
#print app.root_path
#=====================================================================================#
# Document
#=====================================================================================#
@doc.route("doc")
def document():
    #response = make_response(render_template('document.html'))
    response = make_response(render_template('document.html'))
    #response.headers.add('Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')
    return render_template('document.html')


