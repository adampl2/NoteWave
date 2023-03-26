from flask import render_template, request, redirect, url_for, flash
from sweatsmart import app, db


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/logout')
def logout():
    return "<p>logout<p>"


@app.route('/sign-up')
def signup():
    return render_template("sign_up.html")