from io import BytesIO

from plop_app.extensions import db
from plop_app.models import Run

def test_runs_page_shows_empty_message(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"No runs yet" in response.data

def upload(client, name, files):
    return client.post(
        "/runs",
        data={"name": name, "files": [(BytesIO(data), filename) for filename, data in files]},
        content_type="multipart/form-data",
    )

def test_upload_creates_run_and_saves_files(app, client):
    response = upload(client, "Test batch", [("a.jpg", b"one"), ("b.png", b"two")])
    assert response.status_code == 302

    with app.app_context():
        run = db.session.scalars(db.select(Run)).one()
        assert run.name == "Test batch"
        assert len(run.documents) == 2
        for document in run.documents:
            assert (app.config["UPLOAD_FOLDER"] / document.stored_path).is_file()


def test_upload_skips_unsupported_files(app, client):
    upload(client, "Text only", [("notes.txt", b"hello")])

    with app.app_context():
        run = db.session.scalars(db.select(Run)).one()
        assert run.documents == []