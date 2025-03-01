from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = "huush its a secret"

class naming(FlaskForm):
    name = StringField("whats your name", validators=[DataRequired()])
    submit = SubmitField("Submit")

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

@app.route("/name", methods=["GET", "POST"])

def name():
    name = None
    form = naming()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
        flash("form submitted succesfuly")
    return render_template("name.html", name=name, form=form)