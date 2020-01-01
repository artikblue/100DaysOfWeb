from program import app

from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/info')
def info():
    return render_template("info.html")
