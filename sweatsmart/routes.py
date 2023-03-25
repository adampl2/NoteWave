from flask import render_template, request, redirect, url_for, flash
from sweatsmart import app, db


@app.route('/')
def home():
    return "<h1>Test</h1>"