from flask import Flask
from .models import db
from .routes import url_blueprint
import os
from dotenv import load_dotenv

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)

    with app.app_context():
        from . import models  # ensures models are loaded before creating tables
        db.create_all()

    app.register_blueprint(url_blueprint)
    return app
