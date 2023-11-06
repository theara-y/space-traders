from flask import Blueprint

bp = Blueprint('auth', __name__)

if True:
    from app.auth import routes