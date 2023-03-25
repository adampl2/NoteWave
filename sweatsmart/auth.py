from flask import render_template, request, redirect, url_for, flash, Blueprint
from sweatsmart import app, db

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return "<p>login<p>"


@auth.route('/logout')
def logout():
    return "<p>logout<p>"


@auth.route('/sign-up')
def signup():
    return "<p>signup<p>"