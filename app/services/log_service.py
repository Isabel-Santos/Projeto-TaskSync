from app.extensions import mongo_db
from app.models.log import Log
import datetime
from app import db

def create_log(action, user_id):
    log_collection = mongo_db.logs
    log_entry = {'action': action, 'user_id': user_id, 'timestamp': datetime.utcnow()}
    log_collection.insert_one(log_entry)

def get_logs():
    return Log.query.all()
