from app import db, login_manager
import bcrypt
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), index=True, unique=True)
    password = db.Column(db.LargeBinary)
    is_active = db.Column(db.Boolean, default=True)

    def set_password(self, password):
        encoded_password = password.encode('utf-8')
        salt = bcrypt.gensalt(rounds=12)
        hashed_password = bcrypt.hashpw(encoded_password, salt)
        self.password = hashed_password

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password)
    
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))