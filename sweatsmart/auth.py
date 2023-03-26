from flask import render_template, request, redirect, url_for, flash
from sweatsmart import app, db


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@app.route('/logout')
def logout():
    return "<p>logout<p>"


@app.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm-password')

        if len(username) < 2:
            flash('Username must be at least 2 characters', category='error')
        elif len(email) < 4:
            flash('Email must be at least 4 characters', category='error')
        elif password != confirm_password:
            flash('Passwords don\'t match', category='error')
        elif len(password) < 7:
            flash('Password must be at least 7 characters', category='error')
        else:
            flash('Account created successfully', category='success')
    return render_template("sign_up.html")