# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 01:55:05 2020

@author: routm1
"""
from flask import Flask
from myapp.utills import get_instance_folder_path
from myapp.config import configure_app, configure_consol_app
from myapp.cache import cache


app = Flask(
    __name__,
    instance_path=get_instance_folder_path(),
    instance_relative_config=True,
    template_folder="templates",
)

configure_app(app)
cache.init_app(app)
configure_consol_app(app)

#app.config.from_object("environment.DevelopmentConfig")
#port = app.config["PORT"]
#app.config["DEBUG"] = False
#
#server_name = "127.0.0.1:" + port
#app.config["SERVER_NAME"] = server_name
#app.config['SECRET_KEY'] = 'dadjahgdjagjdgsjkt63827fbg'

from myapp import view

