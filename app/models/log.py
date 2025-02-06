from app import db

class Log(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    action = db.Column(db.String(100), nullable = False)
    timestamp = db.Column(db.DateTime, default = db.func.current_timestammp())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    
    user = db.relationship('User', backref = db.backref('logs', lazy = True))

    def __repr__(self):
        return f'<Log {self.action} by {self.user.username}>'