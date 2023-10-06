from flask import Blueprint, request
from flask import jsonify

from marshmallow import ValidationError
from ..schemas.requests.tasks import TaskAdd


todo = Blueprint('todo', __name__, url_prefix="/tasks")


@todo.route('', methods=['POST', 'GET'])
def add_task():
    if request.method == 'POST':
        body = request.json
        schema = TaskAdd()

        try:
            # validate request json
            result = schema.load(body)
        except ValidationError as error:
            return jsonify(error.messages), 400

        return "ok"

    else:
        return "todos"
