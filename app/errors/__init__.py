from flask import Blueprint

bp = Blueprint('errors', __name__)

if True:
    from app.errors import handlers