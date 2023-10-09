from flask import Blueprint, request
from flask import abort, jsonify
from marshmallow import ValidationError

from app.database.db import conn
from app.schemas.requests.tasks import TaskAdd


bp_todo = Blueprint("bp_todo", __name__, url_prefix="/tasks")


@bp_todo.route("", methods=["POST", "GET"])
def add_task():
    if request.method == "POST":
        body = request.json
        schema = TaskAdd()

        try:
            # validate request json
            body = schema.load(body)
            # data = f'({body.get("task")}, {body.get("status_id")}, {body.get("priority_id")}, {body.get("start_date_time")}, {body.get("end_date_time")})'
            cur = conn.cursor()
            cur.execute(
                f"INSERT INTO tasks (task, status_id, priority_id, start_date_time, end_date_time) VALUES(%s, %s, %s, %s, %s) RETURNING id",
                (
                    body.get("task"),
                    body.get("status_id"),
                    body.get("priority_id"),
                    body.get("start_date_time"),
                    body.get("end_date_time"),
                ),
            )
            id_of_new_row = cur.fetchone()[0]
            if id_of_new_row is None:
                abort(400, description="gagal insert data")

            conn.commit()

            return (
                jsonify(status="success", message="insert data berhasil"),
                200,
            )

        except ValidationError as error:
            return jsonify(error.messages), 400

    else:
        cur = conn.cursor()
        cur.execute(
            "SELECT id, task, status_id, priority_id, start_date_time, end_date_time FROM tasks"
        )
        data = cur.fetchall()
        column_name = [
            "id",
            "task",
            "status_id",
            "priority_id",
            "start_date_time",
            "end_date_time",
        ]
        lod_result = [dict(zip(column_name, row)) for row in data]

        return jsonify(lod_result)
