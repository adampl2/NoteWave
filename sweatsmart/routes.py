from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Trip
from . import db
import json

routes = Blueprint('routes', __name__)


@routes.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)


@routes.route("/add_trip", methods=["GET", "POST"])
def add_trip():
    if request.method == "POST":
        trip = Trip(
            trip_name=request.form.get("trip_name"),
            trip_description=request.form.get("trip_description"),
            trip_start_date=request.form.get("trip_start_date"),
            trip_end_date=request.form.get("trip_end_date"),
            id=request.form.get("id")
        )
        db.session.add(trip)
        db.session.commit()
        return redirect(url_for("routes.home"))
    return render_template("home.html", user=current_user)