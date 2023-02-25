#!/usr/bin/python3

import flask
import os

os.environ["FLASK_APP"] = str(__name__)
os.environ["FLASK_DEBUG"] = "true"
app = flask.Flask(__name__, template_folder="../templates/", static_folder="../static/")

@app.route("/")
def render_homepage():
    return flask.render_template("homepage.html")

@app.route("/about")
def render_about():
    return flask.render_template("about.html")

@app.route("/projects")
def render_projects():
    return flask.render_template("projects.html")