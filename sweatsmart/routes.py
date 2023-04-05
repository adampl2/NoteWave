from flask import Blueprint, render_template, request, flash, jsonify
from flask import url_for, redirect
from flask_login import login_required, current_user
from sqlalchemy import desc
from .models import Note
from . import db
import json

routes = Blueprint('routes', __name__)


@routes.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        title = request.form.get('note_title')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        elif len(title) < 1:
            flash('Title is required', category='error')
        else:
            new_note = Note(title=title, data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added successfully!', category='success')
    notes = Note.query.filter_by(
        user_id=current_user.id).order_by(desc(Note.date)).all()

    if len(notes) == 0:
        message = "Your notes will appear here."
    else:
        message = "My Notes"

    return render_template(
        "home.html", user=current_user, notes=notes, message=message)


@routes.route('/delete-note/<int:note_id>', methods=['GET'])
@login_required
def delete_note(note_id):
    note = Note.query.get(note_id)
    if not note or note.user_id != current_user.id:
        return render_template("404.html")
    else:
        db.session.delete(note)
        db.session.commit()
        flash("Your note has been deleted.", category="success")
        return redirect(url_for('routes.home'))


@routes.route("/edit_note/<int:note_id>", methods=["GET", "POST"])
@login_required
def edit_note(note_id):

    note = Note.query.get_or_404(note_id)

    if request.method == "POST":
        note.title = request.form.get("note_title")
        note.data = request.form.get("note")
        db.session.commit()
        flash('Note updated successfully!', category='success')
        return redirect(url_for("routes.home"))
    return render_template("edit_note.html", note=note, user=current_user)
