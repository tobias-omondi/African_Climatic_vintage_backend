from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import flask_bcrypt

db = SQLAlchemy():


class User (db.model):
    id = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String(55), nullable =False)
    email = db.Column(db.String(120), nullable = False)
    password = db.Column(db.String(15) nullable = False)
    subscription = db.Column(db.String)