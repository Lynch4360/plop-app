import uuid
from pathlib import Path

from flask import Blueprint, current_app, redirect, render_template, request, url_for

from plop_app.extensions import db
from plop_app.models import Run, Document

bp = Blueprint("main", __name__)

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".pdf", ".heic"}


# This will show previous runs (uploaded batches) but
# it's just a placeholder for flask setup
@bp.route("/")
def runs():
    all_runs = db.session.scalars(db.select(Run).order_by(Run.created_at.desc())).all()
    return render_template("main/runs.html", runs=all_runs)


@bp.post("/runs")
def create_run():
    run = Run(name=request.form.get("name", "").strip() or "Untitled run")
    db.session.add(run)
    db.session.flush()

    upload_dir = Path(current_app.instance_path) / "uploads" / str(run.id)
    upload_dir.mkdir(parents=True, exist_ok=True)

    for file in request.files.getlist("files"):
        extension = Path(file.filename or "").suffix.lower()
        if extension not in ALLOWED_EXTENSIONS:
            continue
        stored_name = f"{uuid.uuid4().hex}{extension}"
        file.save(upload_dir / stored_name)
        run.documents.append(
            Document(filename=file.filename, stored_path=f"{run.id}/{stored_name}")
        )
    db.session.commit()
    return redirect(url_for("main.runs"))


@bp.route("/analysis")
def analysis():
    return render_template("main/analysis.html")
