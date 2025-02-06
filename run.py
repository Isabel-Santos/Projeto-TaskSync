from app import create_app
from flask_migrate import Migrate
from flask.cli import with_appcontext
import click
from app.extensions import db
from flask_cors import CORS


app = create_app()
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)

