#!/usr/bin/python3

import flask
import os
import sys


os.environ["FLASK_APP"] = str(__name__)
os.environ["FLASK_DEBUG"] = "true"
app = flask.Flask(__name__)



@app.route("/")
def hello_world():
    return "hello world from the server!"