from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime

db = SQLAlchemy()
bcrypt = Bcrypt()

# User Table
class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(55), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    subscription = db.Column(db.Boolean, default=False)

# Admin Table
class Admin(db.Model):

    __tablename__ = 'Admin'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(55), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    

    # Relationship
    news = db.relationship('News', backref = 'admin', lazy =True)
    documentation = db.relationship('Documentation', backref = 'admin', lazy = True)
    multimedia = db.relationship('Multimedia', backref = 'admin', lazy = True)
    podcast = db.relationship('Podcast', backref = 'admin', lazy = True )
    panel_discusion = db.relationship('Panel_Discusion', backref = 'admin' , lazy = True)
    interview = db.relationship ('Interview', backref = 'admin' , lazy = True)

# News Table
class News(db.Model):
    __tablename__ = 'News'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(2000))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)

# Documentation Table
class Documentation(db.Model):

    __tablename__ = 'Documentation'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    content_type = db.Column(db.String(50), nullable=False)  # E.g., 'PDF', 'DOC'
    file_path = db.Column(db.String(255))
    file_url = db.Column(db.String(255))
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)

    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)

# Multimedia Table
class Multimedia(db.Model):

    __tablename__ = 'Multimedia'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    content_type = db.Column(db.String(50), nullable=False)  # E.g., 'image', 'video'
    file_path = db.Column(db.String(255))
    file_url = db.Column(db.String(255))
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)

    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)

# Podcast Table
class Podcast(db.Model):

    __tablename__ = 'Podcast'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    audio_url = db.Column(db.String(255), nullable=False)
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)

    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)

# Panel Discussion Table
class Panel_Discussion(db.Model):

    __tablename__ = 'PanelDiscussion'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    panel_list = db.Column(db.Text)  # List of panelists, can be stored as a string or JSON
    video_file_path = db.Column(db.String(255))

   admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)

# Interview Table
class Interview(db.Model):

    __tablename__ = '
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(255), nullable=False)

   admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)