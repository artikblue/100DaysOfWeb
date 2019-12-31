from program import app

@app.route('/')
@app.route('/index')
def index():
    return "<h1>First flask app :)</h1>"

@app.route('/info')
def info():
    return "<b>this is the info page</b>"
