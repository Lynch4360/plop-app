from flask import Blueprint, render_template

bp = Blueprint("main", __name__)

# This will show previous runs (uploaded batches) but
# it's just a placeholder for flask setup
@bp.route("/")
def runs():
    return render_template("main/runs.html")

@bp.route("/analysis")
def analysis():
    return render_template("main/analysis.html")