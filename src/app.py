#!/usr/bin/python3

import flask
import os
import json

os.environ["FLASK_APP"] = str(__name__)
os.environ["FLASK_DEBUG"] = "true"
# app = flask.Flask(__name__, template_folder="../templates/", static_folder="../static/")
app = flask.Flask(__name__, root_path=os.path.abspath(os.path.join(os.getcwd(), '..')))
print(app.root_path)

@app.route("/")
def render_homepage():
    return flask.render_template("homepage.html")

@app.route("/about")
def render_about():
    return flask.render_template("about.html")

@app.route("/projects")
def render_projects():
    return flask.render_template("projects.html")

@app.route("/oats")
def retrieve_github_token():
    with open("static/tokens.json") as f:
        data = json.load(f)
        token = data.get("github", None)
        if token is not None:
            return token
        else:
            return "None"