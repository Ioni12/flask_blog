from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def index():
    first_name = "Joni"
    stuff = "dont worry this is <h1>me</h1>"
    more_stuff = [ "dont know what to add", "joni", 34, "add them all" ]
    return render_template("index.html", first_name=first_name, stuff=stuff, more_stuff=more_stuff)

@app.route("/user/<name>")

def user(name):
    return render_template("user.html", user_name=name)

#invalid url
@app.errorhandler(404)

def page_not_found(e):
    return render_template("404.html"), 404

#eternal server error
@app.errorhandler(500)

def page_not_found(e):
    return render_template("500.html"), 500