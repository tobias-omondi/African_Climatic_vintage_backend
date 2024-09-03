from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_basicauth import BasicAuth
from flask_login import LoginManager
from .modelviews import UserAdminView


db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # Configure SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Africa_climatic_database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Configure BasicAuth
    app.config['BASIC_AUTH_USERNAME'] = 'admin'
    app.config['BASIC_AUTH_PASSWORD'] = 'password'
    basic_auth = BasicAuth(app)

    # Configure Flask-Login
    app.config['SECRET_KEY'] = 'your_secret_key'  # Required for session management
    login_manager.init_app(app)
    login_manager.login_view = 'login'  # Specify the login route
    login_manager.login_message_category = 'info'  # Flash message category

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    # Import models
    import myapp.models
    User, News, Documentation, PanelDiscussion, Interview, AdminModel, Multimedia, Podcast = (
        myapp.models.User,
        myapp.models.News,
        myapp.models.Documentation,
        myapp.models.PanelDiscussion,
        myapp.models.Interview,
        myapp.models.Admin,
        myapp.models.Multimedia,
        myapp.models.Podcast,
    )

    # Flask-Admin initialization
    admin = Admin(app, name='microblog', template_mode='bootstrap4')

    # Add administrative views
    admin.add_view(UserAdminView(User, db.session))
    admin.add_view(ModelView(News, db.session))
    admin.add_view(ModelView(Documentation, db.session))
    admin.add_view(ModelView(Multimedia, db.session))
    admin.add_view(ModelView(Podcast, db.session))
    admin.add_view(ModelView(PanelDiscussion, db.session))
    admin.add_view(ModelView(Interview, db.session))

    # Create tables if they don't exist
    with app.app_context():
        db.create_all()

    return app
