import pytest
from plop_app import create_app
from plop_app.extensions import db

@pytest.fixture
def app(tmp_path):
    app = create_app(
        {
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": f"sqlite:///{tmp_path / 'test.db'}",
            "UPLOAD_FOLDER": tmp_path / "uploads"
        }
    )
    with app.app_context():
        db.create_all()
        yield app

@pytest.fixture
def client(app):
    return app.test_client()