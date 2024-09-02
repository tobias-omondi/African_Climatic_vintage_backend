from flask import Flask
from flask_restful import Resource, Api
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.model import User, News, Documentation, PanelDiscussion, Interview, Admin, Multimedia, Podcast, bcrypt

app = Flask(__name__)
api = Api(app)

# Configure SQLite database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Africa climatic database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Correctly initialize Migrate

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True, port=5500)  # Correctly set debug mode and port
