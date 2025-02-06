from flask import Blueprint, send_from_directory, current_app
import os

bp = Blueprint('frontend', __name__, url_prefix='/')

@bp.route('/', defaults={'path': ''})
@bp.route('/<path:path>')
def serve_react(path):
    react_build_path = os.path.join(current_app.root_path, 'frontend', 'build')
    
    if path != "" and os.path.exists(os.path.join(react_build_path, path)):
        return send_from_directory(react_build_path, path)
    else:
        return send_from_directory(react_build_path, 'index.html')