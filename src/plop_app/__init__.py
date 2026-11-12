import os

from flask import Flask
from plop_app import models
from plop_app.extensions import db, migrate
from plop_app.main import bp as main_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "DATABASE_URL", "sqlite:///app.db"
    )
    app.config["MAX_CONTENT_LENGTH"] = 50 * 1024 * 1024

    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    app.register_blueprint(main_bp)
    return app
