from flask import Blueprint, render_template

from plop_app.extensions import db
from plop_app.models import Run

bp = Blueprint("main", __name__)

# This will show previous runs (uploaded batches) but
# it's just a placeholder for flask setup
@bp.route("/")
def runs():
    all_runs = db.session.scalars(
        db.select(Run).order_by(Run.created_at.desc())
    )
    return render_template("main/runs.html", runs=all_runs)

@bp.route("/analysis")
def analysis():
    return render_template("main/analysis.html")