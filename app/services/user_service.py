from . .models.user import User
from app import db
import bcrypt 

def create_user(username, email, password):
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    user = User(username = username, email = email, password_hash = password_hash)
    db.session.add(user)
    db.session.commit()
    return user

def get_users():
    return User.query.all()