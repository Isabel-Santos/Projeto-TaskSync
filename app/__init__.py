from flask import Flask, render_template
from flask_login import LoginManager, login_required
from app.extensions import db, jwt, login_manager, cache
from app.config import Config
from .routes import auth, user, task, log
from .models.user import User


def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    login_manager.init_app(app)
    cache.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/homepage')
    @login_required
    def homepage():
        return render_template('homepage.html')

    app.register_blueprint(auth.bp)
    app.register_blueprint(user.bp)
    app.register_blueprint(task.bp)
    app.register_blueprint(log.bp)

    return app