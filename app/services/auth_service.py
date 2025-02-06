from app.models.user import User
from app import db
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from datetime import datetime, timedelta

def authenticate_user(username, password):
    user = User.query.filter_by(username = username).first()
    if user and check_password_hash(user.password, password):
        token = create_access_token(identity=user.id)
        return {"access_token": token}, 200
    return {"error": "Invalid credentials"}, 401