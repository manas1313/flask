# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 02:45:31 2020

@author: routm1
"""

from myapp import app
from gevent.pywsgi import WSGIServer

#app.config['DEBUG']= True

if __name__ == "__main__":
    
    if app.config["ENV"] == "production":
        app.config.from_object("config.ProductionConfig")
        http_server = WSGIServer(('', 5000), app)
        http_server.serve_forever()
    else:
        app.config.from_object("config.DevelopmentConfig")

    print(f'ENV is set to: {app.config["ENV"]}')
    
    app.run()
#    app.run(debug = app.debug)
