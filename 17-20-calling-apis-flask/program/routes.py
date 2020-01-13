from program import app
from flask import render_template

from datetime import datetime

import requests


@app.route('/')
@app.route('/index')
def index():
    timenow = str(datetime.today())
    return render_template("index.html", time=timenow)

@app.route('/info')
def info():
    return render_template("info.html")

@app.route('/chuck')
def chuck_api():
    chuck_api_url = "https://api.chucknorris.io/jokes/random"
    new_joke = requests.get(chuck_api_url)

    return render_template("chuck.html", joke=new_joke.json())