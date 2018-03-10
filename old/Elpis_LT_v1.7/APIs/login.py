# -*- coding: utf-8 -*-
from flask import Module, render_template, make_response,url_for,request,session,redirect,Blueprint
import json
app = Blueprint('login', __name__, url_prefix='/',template_folder='templates',static_folder='static')

USER_PASSWORD = "pass"

@app.route('')
def logsite():
    return render_template('login.html')
   

@app.route('/login', methods=['GET', 'POST'])
def login():
    #print config.USER_NAME 
    if request.method == 'POST':
        session['password'] = request.form['password']
        #session['user'] = request.form['user']
        if session['password'] == USER_PASSWORD :   
                return redirect(url_for('root.index'))
    return redirect(url_for('login.logsite'))
        
    #return redirect(url_for('logout'))

@app.route('/logout')
def logout():
    # remove the username from the session if its there
    session.pop('password', None)
    return redirect(url_for('root.index'))
