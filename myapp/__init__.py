from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_admin import Admin as FlaskAdmin
from flask_admin.contrib.sqla import ModelView
import os

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()
admin = FlaskAdmin()

def create_app():
    app = Flask(__name__)

    # Configure app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Africa_climatic_database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_default_secret_key')
    app.config['BASIC_AUTH_USERNAME'] = os.getenv('BASIC_AUTH_USERNAME', 'admin')
    app.config['BASIC_AUTH_PASSWORD'] = os.getenv('BASIC_AUTH_PASSWORD', 'password')

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    admin.init_app(app)

    # Import models here to avoid circular imports
    from myapp.models import User, AdminUser, News, Documentation, Multimedia, Podcast, PanelDiscussion, Interview

    # Add views to Flask-Admin
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(AdminUser, db.session))
    admin.add_view(ModelView(News, db.session))
    admin.add_view(ModelView(Documentation, db.session))
    admin.add_view(ModelView(Multimedia, db.session))
    admin.add_view(ModelView(Podcast, db.session))
    admin.add_view(ModelView(PanelDiscussion, db.session))
    admin.add_view(ModelView(Interview, db.session))

    # Load User model for login
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))  # Consider changing to AdminUser if that's your intention
    
    # Create tables if they don't exist
    with app.app_context():
        db.create_all()

    return app
