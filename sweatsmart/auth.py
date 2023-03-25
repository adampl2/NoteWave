from flask import render_template, request, redirect, url_for, flash
from sweatsmart import app, db


@app.route('/login')
def login():
    return "<p>login<p>"


@app.route('/logout')
def logout():
    return "<p>logout<p>"


@app.route('/sign-up')
def signup():
    return "<p>signup<p>"