from flask import Flask
from plop_app.main import bp as main_bp

def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(main_bp)
    return app
