from flask import Flask
from flask import jsonify

from .routes.tasks import todo
from .routes.status import statuses
from .routes.priorities import bp_priorities


app = Flask(__name__)
app.register_blueprint(todo)
app.register_blueprint(statuses)
app.register_blueprint(bp_priorities)


@app.errorhandler(404)
def not_found_error_handler(e):
    return jsonify(error=str(e)), 404


@app.route('/')
def index():
    return "Welcome"
