from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash as gph
from werkzeug.security import check_password_hash
from . import db   # means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return "<p>logout<p>"


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
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
            new_user = User(
                email=email, username=username, password=gph(
                    password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully', category='success')
            return redirect(url_for('routes.home'))
    return render_template("sign_up.html")