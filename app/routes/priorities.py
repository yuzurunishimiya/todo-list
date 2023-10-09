from flask import Blueprint
from flask import abort, jsonify

from app.database.db import conn


bp_priorities = Blueprint("bp_priorities", __name__, url_prefix="/priorities")


@bp_priorities.route("", methods=["GET"])
def get_priorities():
    cur = conn.cursor()
    cur.execute("SELECT id, priority FROM priorities")
    data = cur.fetchall()

    column_name = ["id", "priority"]
    lod_result = [dict(zip(column_name, row)) for row in data]

    return jsonify(lod_result)


@bp_priorities.route("/<int:priority_id>", methods=["GET"])
def get_priority(priority_id):
    cur = conn.cursor()
    cur.execute(
        "SELECT id, priority FROM priorities WHERE id={}".format(priority_id)
    )
    datum = cur.fetchone()

    if datum is None:
        abort(404, description="Resource not found")

    return jsonify(id=datum[0], priority=datum[1])
