from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
from flask_caching import Cache
from sqlalchemy.pool import QueuePool

db = SQLAlchemy()
jwt = JWTManager()
login_manager = LoginManager()
client = MongoClient('mongodb://localhost:27017/')
mongo_db = client['tasksync_db']
cache = Cache()

login_manager.login_view = 'auth.login'
login_manager.login_message = "Por favor, faça login para acessar esta página."
login_manager.login_message_category = "warning"


"""
    engine_options={
        "poolclass": QueuePool,  
        "pool_size": 10,         
        "max_overflow": 5,       
        "pool_timeout": 30,      
        "pool_recycle": 1800     
    }"""