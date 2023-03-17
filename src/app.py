#!/usr/bin/python3

import flask
import os
import json

os.environ["FLASK_APP"] = str(__name__)
os.environ["FLASK_DEBUG"] = "true"
rootpath = os.path.abspath(os.path.join(os.getcwd(), '..'))

app = flask.Flask(__name__, root_path=rootpath)
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

@app.route("/oauth_gh_token")
def retrieve_github_token():
    with open(f"{rootpath}/static/tokens.json") as f:
        data = json.load(f)
        token = data.get("github_full_access", None)
        if token is not None:
            return token
        else:
            return "None"