import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'cc686aa971e8505642002cb8de9a73d3')

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///tasksync.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'jwt_secret')
    JWT_ACESS_TOKEN_EXPIRES = 3600

    CACHE_TYPE = 'redis'
    CACHE_REDIS_URL = 'redis://localhost:6379/0'
    CACHE_DEFAULT_TIMEOUT = 300

"""    SQLALCHEMY_ENGINE_OPTIONS = {
        "poolclass": "QueuePool",
        "pool_size": 10,
        "max_overflow": 5,
        "pool_timeout": 30,
        "pool_recycle": 1800
    }    GOOGLE_CLIENT_ID = "SEU_CLIENT_ID"
    GOOGLE_CLIENT_SECRET = "SEU_CLIENT_SECRET" 
"""
