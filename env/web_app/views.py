from datetime import datetime
from flask import render_template
from web_app import app

@app.route('/')
@app.route('/index')
def index():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    return render_template(
        "index.html",
        title = "ElGuada90",
        message = "Bienvenidos",
        content = " on " + formatted_now)
    

@app.route('/micanal')
def micanal():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    return render_template(
        "micanal.html",
        title = "ElGuada90",
        message = "Top Apps",
        content = " on " + formatted_now)