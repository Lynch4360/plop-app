from flask import Blueprint, redirect, render_template

bp = Blueprint("main", __name__)

# I can't think of a better name than runs right now
# This will show previous documents that have been computed but
# it's just a placeholder for flask setup
@bp.route("/")
def runs():
    return render_template("main/runs.html")