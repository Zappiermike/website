#!/usr/bin/python3

import flask
import os


os.environ["FLASK_APP"] = str(__name__)
os.environ["FLASK_DEBUG"] = "true"
app = flask.Flask(__name__, template_folder="../templates/", static_folder="../static/")



@app.route("/")
def hello_world():
    return flask.render_template("homepage.html")