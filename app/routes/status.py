from flask import Blueprint
from flask import abort, jsonify

# pylint: disable=E0611
from app.database.db import conn


statuses = Blueprint('status', __name__, url_prefix="/status")


@statuses.route('', methods=["GET"])
def get_statuses():
    cur = conn.cursor()
    cur.execute("SELECT id, status FROM statuses")
    data = cur.fetchall()

    column_name = ['id','status']
    lod_result = [dict(zip(column_name, row)) for row in data]

    return jsonify(lod_result)


@statuses.route("/<int:status_id>", methods=["GET"])
def get_status(status_id):
    cur = conn.cursor()
    cur.execute("SELECT id, status FROM statuses WHERE id={}".format(status_id))
    datum = cur.fetchone()

    if datum is None:
        abort(404, description="Resource not found")

    return jsonify(id=datum[0], status=datum[1])
