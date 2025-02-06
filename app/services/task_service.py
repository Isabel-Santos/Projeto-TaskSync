from flask import jsonify
from app.models.task import Task
from app.extensions import db, cache
from app import db

def create_task(title, description, user_id):
    task = Task(title = title, description = description, user_id = user_id)
    db.session.add(task)
    db.session.commit()
    return {"message": "Tarefa criada com sucesso"}, 201

def get_tasks():
    return Task.query.all()

def get_task_by_id(task_id):
    task = cache.get(f"task:{task_id}")
    if task:
        return task

def get_tasks_by_title(title):
    return Task.query.filter(Task.title.ilike(f"%{title}%")).all()

def get_tasks_by_status(status):
    return Task.query.filter_by(status = status).all()

def get_tasks_by_criteria(task_id=None, title=None, status=None):
    query = Task.query
    if task_id:
        query = query.filter(Task.id == task_id)
    if title:
        query = query.filter(Task.title.ilike(f'%{title}%'))
    if status:
        query = query.filter(Task.status == status)
    return query.all()

def update_task(task, title=None, description=None):
    if title:
        task.title = title
    if description:
        task.description = description

    db.session.commit()
    return task

def delete_task(task):
    db.session.delete(task)
    db.session.commit()

def get_task_from_cache(task_id):
    task = cache.get(f"task:{task_id}")
    if task:
        return task
    task = Task.query.get(task_id)
    if task:
        task_data = {"id": task.id, "title": task.title, "description": task.description, "user_id": task.user_id}
        cache.set(f"task:{task_id}", task_data)
        return task_data
    return None