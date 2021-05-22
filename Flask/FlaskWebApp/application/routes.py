from flask import render_template
from application import app, db


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/login')
def login():
    return "<h1>Login Page</h1>"


@app.route('/logout')
def logout():
    return "<h1>You have logout</h1>"


@app.route('/sign-up')
def signup():
    return "<h1>Here you can create a new account</h1>"
