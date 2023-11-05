from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    # Register blueprints
    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)
    
    from app.users import bp as users_bp
    app.register_blueprint(users_bp, url_prefix='/users')


    return app