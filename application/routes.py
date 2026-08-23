from application import app

from flask import render_template, url_for, request

@app.route("/")
def home():
    usuario = "UserDev"
    context = {
        "usuario": usuario,
    }
    return render_template("index.html", context = context)

@app.route("/contact", methods=["GET", "POST"])
def con():
    context = {}
    if request.method == "GET":
        research = request.args.get("research")
        context.update({"research":research})
    if request.method == "POST":
            research = request.args.get("research")
            context.update({"research":research})
    return render_template("contact.html", context=context)
