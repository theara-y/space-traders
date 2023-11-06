from app.users import bp
from app.models import User
from app import db
from flask import render_template, redirect, url_for
from flask_login import login_required

@bp.route('/')
@login_required
def get_users():
    users = User.query.all()
    return render_template('users.html', users=users)
    