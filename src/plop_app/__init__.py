import os

from flask import Flask
from pathlib import Path
from plop_app import models
from plop_app.extensions import db, migrate
from plop_app.main import bp as main_bp


def create_app(test_config: dict | None = None) -> Flask:
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "DATABASE_URL", "sqlite:///app.db"
    )
    app.config["MAX_CONTENT_LENGTH"] = 50 * 1024 * 1024
    app.config["UPLOAD_FOLDER"] = Path(app.instance_path) / "uploads"

    if test_config is not None:
        app.config.update(test_config)

    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    app.register_blueprint(main_bp)
    return app
