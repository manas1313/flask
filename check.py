# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 19:20:01 2020

@author: routm1
"""

import os
from flask import Flask
from healthcheck import HealthCheck, EnvironmentDump
from myapp.config import config

app = Flask(__name__)
config_name = os.getenv("FLASK_CONFIGURATION", "default")
app.config.from_object(config[config_name])
app.config.from_pyfile("config.cfg", silent=True)

envdump = EnvironmentDump(
    app,
    "/environment",
    include_python=True,
    include_os=False,
    include_process=False,
    include_config=True,
)

def application_data():
    return {
        "maintainer": "Damyan Bogoev",
        "git_repo": "https://github.com/anz-ecp/manas1313.git",
    }
    
envdump.add_section("application", application_data)

if __name__ == "__main__":
    app.run(host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", 8080)))