from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shortURL = db.Column(db.String(31), unique=True, nullable=False)
    longURL = db.Column(db.String(255), nullable=False)
