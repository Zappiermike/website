#!/usr/bin/python3

import flask
import os
import json
import requests

os.environ["FLASK_APP"] = str(__name__)
os.environ["FLASK_DEBUG"] = "true"
rootpath = os.path.abspath(os.path.join(os.getcwd(), '..'))

app = flask.Flask(__name__, root_path=rootpath)

@app.route("/")
def render_homepage():
    return flask.render_template("homepage.html")

@app.route("/about")
def render_about():
    return flask.render_template("about.html")

@app.route("/projects")
def render_projects():
    return flask.render_template("projects.html")

@app.route("/github_repositories", methods=["POST", "GET"])
def gh_repos():
    username = "zappiermike"
    token = retrieve_github_token()
    Headers = {
        'X-GitHub-Api-Version': '2022-11-28',
        'Authorization': 'token ' + token
    }
    # print(Headers)
    repo_list = requests.get(f"https://api.github.com/users/{username}/repos", headers=Headers)
    return {"repo_list": repo_list.json()}



def retrieve_github_token():
    token = os.environ.get("GITHUB_TOKEN", None)
    # print(token)
    return token

