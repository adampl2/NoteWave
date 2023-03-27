from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Trip(db.Model):
    # schema for the Trip model
    id = db.Column(db.Integer, primary_key=True)
    trip_name = db.Column(db.String(50), unique=True, nullable=False)
    trip_description = db.Column(db.Text, nullable=False)
    trip_start_date = db.Column(db.Date, nullable=False)
    trip_end_date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return
        f"#{self.id} - Task: {self.trip_name}"


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    username = db.Column(db.String(120))
    trip = db.relationship('Trip')
