from app.users import bp
from flask import render_template, redirect, url_for
from app.models import User
from app import db

@bp.route('/')
def get_users():
    users = User.query.all()
    return render_template('users.html', users=users)
    