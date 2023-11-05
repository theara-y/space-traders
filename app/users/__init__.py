from flask import Blueprint

bp = Blueprint('users', __name__)

if True:
    from app.users import routes