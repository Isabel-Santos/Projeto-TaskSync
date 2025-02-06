from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash, session, current_app
from flask_login import login_user, logout_user, login_required
from app.models.user import User
from app.services.auth_service import authenticate_user
from werkzeug.security import generate_password_hash
from app import db
"""from authlib.integrations.flask_client import OAuth
"""

bp = Blueprint('auth', __name__, url_prefix = '/auth')


@bp.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@bp.route('/login', methods=['POST'])
def auth_login():
    data = request.get_json()

    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'message': 'Username e senha são obrigatórios!'}), 400

    token = authenticate_user(data['username'], data['password'])
    
    if token:
        return jsonify({'token': token}), 200
    return jsonify({'message': 'Credenciais inválidas!'}), 401



@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        data = request.get_json()
        
        if not data or 'username' not in data or 'email' not in data or 'password' not in data:
            return jsonify({'message': 'Todos os campos são obrigatórios!'}), 400

        user = User.query.filter_by(email=data['email']).first()
        
        if user:
            return jsonify({'message': 'Email já cadastrado!'}), 409

        new_user = User(username=data['username'], email=data['email'])
        new_user.set_password(generate_password_hash(data['password'], method="pbkdf2:sha256"))
        
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({'message': 'Usuário cadastrado com sucesso!'}), 201
    else:
        return render_template('signup.html')


@bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logout realizado com sucesso!'}), 200