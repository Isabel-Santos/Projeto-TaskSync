from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from app.services.task_service import create_task, get_tasks, get_task_by_id, update_task, delete_task

bp = Blueprint('task', __name__, url_prefix = '/tasks')

@bp.route('/', methods=['POST'])
@login_required
def add_task():
    data = request.get_json()

    if not data or 'title' not in data or 'description' not in data:
        return jsonify({'message': 'Título e descrição são obrigatórios!'}), 400

    task = create_task(data['title'], data['description'], current_user.id)
    return jsonify({'message': 'Tarefa criada com sucesso!', 'task_id': task.id}), 201

@bp.route('/', methods=['GET'])
@login_required
def list_tasks():
    tasks = get_tasks(user_id=current_user.id)
    return jsonify([{'id': task.id, 'title': task.title, 'description': task.description, 'status': task.status} for task in tasks]), 200

@bp.route('/<int:task_id>', methods=['GET'])
@login_required
def get_task(task_id):
    task = get_task_by_id(task_id)

    if not task or task.user_id != current_user.id:
        return jsonify({'message': 'Tarefa não encontrada ou acesso negado!'}), 404

    return jsonify({'id': task.id, 'title': task.title, 'description': task.description, 'status': task.status}), 200

@bp.route('/<int:task_id>', methods=['PUT'])
@login_required
def edit_task(task_id):
    data = request.get_json()
    task = get_task_by_id(task_id)

    if not task or task.user_id != current_user.id:
        return jsonify({'message': 'Tarefa não encontrada ou acesso negado!'}), 404

    updated_task = update_task(task, data.get('title'), data.get('description'))
    return jsonify({'message': 'Tarefa atualizada!', 'task': {'id': updated_task.id, 'title': updated_task.title, 'description': updated_task.description, 'status': updated_task.status}}), 200

@bp.route('/<int:task_id>', methods=['DELETE'])
@login_required
def remove_task(task_id):
    task = get_task_by_id(task_id)

    if not task or task.user_id != current_user.id:
        return jsonify({'message': 'Tarefa não encontrada ou acesso negado!'}), 404

    delete_task(task)
    return jsonify({'message': 'Tarefa deletada com sucesso!'}), 200