from flask import Blueprint, request, jsonify
from app.services.user_service import create_user, get_users

bp = Blueprint('user', __name__, url_prefix = '/users')

@bp.route('/', methods=['GET'])
def list_users():
    users = get_users()
    return jsonify([{'id': user.id, 'username': user.username, 'email': user.email} for user in users]), 200

@bp.route('/', methods=['POST'])
def add_user():
    data = request.get_json()
    
    if not data or 'username' not in data or 'email' not in data or 'password' not in data:
        return jsonify({'message': 'Todos os campos são obrigatórios!'}), 400

    user = create_user(data['username'], data['email'], data['password'])
    return jsonify({'message': 'Usuário criado com sucesso!', 'user_id': user.id}), 201