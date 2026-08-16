from application import app

from flask import render_template, url_for

@app.route("/")
def home():
    usuario = "UserDev"
    context = {
        "usuario": usuario,
    }
    return render_template("index.html", context = context)

@app.route("/contact")
def con():
    return render_template("contact.html")
