from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
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

    return render_template("home.html", user=current_user)


@routes.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})