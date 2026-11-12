from datetime import datetime, timezone

from plop_app.extensions import db


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class Run(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=utc_now)

    documents = db.relationship(
        "Document", back_populates="run", cascade="all, delete-orphan"
    )


class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    run_id = db.Column(db.Integer, db.ForeignKey("run.id"), nullable=False)
    filename = db.Column(db.String(250), nullable=False)
    stored_path = db.Column(db.String(500), nullable=False)
    doc_type = db.Column(db.String(20))

    run = db.relationship("Run", back_populates="documents")
