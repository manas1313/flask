# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 14:34:26 2020

@author: routm1
"""

from myapp import app
from flask import render_template, json, Blueprint, jsonify
from appenv import infosetup
import subprocess
import getpass
import sys


errors = Blueprint('errors', __name__)
#app.app_context()
#loglevel = app.config.get("LOGGING_LEVEL")
#info_dict = infosetup.info()
#port = app.config.get("PORT")

def logg_level(level):   
    
    return 'DEBUG' if level == 10 else 'INFO' if level == 20 else 'WARNING' if level == 30 else 'ERROR' if level == 40 else 'CRITICAL' if level == 50 else 'NOTSET'

def getgithead():
    
    try:
        process = subprocess.Popen(['git', 'rev-parse', 'HEAD'], shell=False, stdout=subprocess.PIPE)
        git_head_hash = process.communicate()[0].strip().hex()
    except:
        git_head_hash = "Not Available"
    return git_head_hash

def response():
    loglevel = app.config.get("LOGGING_LEVEL")
    info_dict = infosetup.info()
    port = app.config.get("PORT")
    lg_level =logg_level(loglevel) 
    git_head= getgithead()
    appinfo_dist={}
    
    try:
        appinfo_dist = {"name": info_dict['name'], "version" : info_dict['version'],"git_commit_sha": git_head, "environment": {"service_port" : port, "log_level" : lg_level}}
    except:
        appinfo_dist = {}
    return appinfo_dist

@app.route("/")
def index():
    return render_template('home.html') 

@app.route('/info', methods=['GET','POST'])
def info():
    
#    print("Information page loaded successfully by {0} ".format(getpass.getuser()), file = sys.stderr)
    resp = json.dumps(response(), separators=(',', ': '), indent=2)    
    return resp

@errors.app_errorhandler(Exception)
def handle_error(error):
    message = [str(x) for x in error.args]
    status_code = error.status_code
    success = False
    response = {
        'success': success,
        'error': {
            'type': error.__class__.__name__,
            'message': message
        }
    }

    return jsonify(response), status_code

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

#@app.before_request
#def brequest():
#    return sys.stdout("Information page loaded successfully by {0} ".format(getpass.getuser()))
    



    


