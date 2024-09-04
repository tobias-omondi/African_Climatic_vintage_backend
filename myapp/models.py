from datetime import datetime
from sqlalchemy.orm import validates
import re
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin
from myapp import db, bcrypt

# User Table
class User(db.Model, SerializerMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(55), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    message = db.Column(db.String(1000), nullable=False)

    @validates('email')
    def validate_email(self, key, email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email address")
        return email

    def __repr__(self):
        return '<User %r>' % (self.full_name)

# Admin User Table
class AdminUser(db.Model, SerializerMixin, UserMixin):
    __tablename__ = 'admin_user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(55), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    # Relationships
    news = db.relationship('News', backref='admin', lazy=True)
    documentation = db.relationship('Documentation', backref='admin', lazy=True)
    multimedia = db.relationship('Multimedia', backref='admin', lazy=True)
    podcast = db.relationship('Podcast', backref='admin', lazy=True)
    panel_discussion = db.relationship('PanelDiscussion', backref='admin', lazy=True)
    interview = db.relationship('Interview', backref='admin', lazy=True)

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def __repr__(self):
        return '<AdminUser %r>' % (self.username)

# News Table
class News(db.Model, SerializerMixin):
    __tablename__ = 'news'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(2000))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    admin_id = db.Column(db.Integer, db.ForeignKey('admin_user.id'), nullable=True)

    @validates('title')
    def validate_title(self, key, title):
        if len(title) < 5:
            raise ValueError("Title must be at least 5 characters long")
        return title

# Documentation Table
class Documentation(db.Model, SerializerMixin):
    __tablename__ = 'documentation'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    content_type = db.Column(db.String(50), nullable=True)  # E.g., 'PDF', 'DOC'
    file_path = db.Column(db.String(255), nullable=True)
    file_url = db.Column(db.String(255))
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)

    admin_id = db.Column(db.Integer, db.ForeignKey('admin_user.id'), nullable=True)

    @validates('content_type')
    def validate_content_type(self, key, content_type):
        allowed_types = ['PDF', 'DOC', 'DOCX']
        if content_type.upper() not in allowed_types:
            raise ValueError(f"Content type must be one of {', '.join(allowed_types)}")
        return content_type

# Multimedia Table
class Multimedia(db.Model, SerializerMixin):
    __tablename__ = 'multimedia'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    content_type = db.Column(db.String(255), nullable=True)  # E.g., 'image', 'video'
    file_path = db.Column(db.String(255), nullable=True)
    file_url = db.Column(db.String(255))
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)

    admin_id = db.Column(db.Integer, db.ForeignKey('admin_user.id'), nullable=True)

    @validates('content_type')
    def validate_content_type(self, key, content_type):
        allowed_types = ['image', 'video', 'audio']
        if content_type.lower() not in allowed_types:
            raise ValueError(f"Content type must be one of {', '.join(allowed_types)}")
        return content_type

# Podcast Table
class Podcast(db.Model, SerializerMixin):
    __tablename__ = 'podcast'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    audio_url = db.Column(db.String(255), nullable=False)
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)

    admin_id = db.Column(db.Integer, db.ForeignKey('admin_user.id'), nullable=True)

# Panel Discussion Table
class PanelDiscussion(db.Model, SerializerMixin):
    __tablename__ = 'paneldiscussion'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    panel_list = db.Column(db.Text)  # List of panelists, can be stored as a string or JSON
    video_file_path = db.Column(db.String(255))

    admin_id = db.Column(db.Integer, db.ForeignKey('admin_user.id'), nullable=True)

# Interview Table
class Interview(db.Model, SerializerMixin):
    __tablename__ = 'interview'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(255), nullable=False)

    admin_id = db.Column(db.Integer, db.ForeignKey('admin_user.id'), nullable=True)
