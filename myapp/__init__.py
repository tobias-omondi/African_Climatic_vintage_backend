from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)

    # Configure SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Africa_climatic_database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    # Import models
    import myapp.models

    with app.app_context():
        User, News, Documentation, PanelDiscussion, Interview, Admin, Multimedia, Podcast = \
            myapp.models.User, myapp.models.News, myapp.models.Documentation, myapp.models.PanelDiscussion, \
            myapp.models.Interview, myapp.models.Admin, myapp.models.Multimedia, myapp.models.Podcast

        # Create tables if they don't exist
        db.create_all()

    return app
