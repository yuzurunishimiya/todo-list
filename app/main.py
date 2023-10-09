from flask import Flask
from flask import jsonify

from .routes.tasks import bp_todo
from .routes.priorities import bp_priorities
from .routes.statuses import bp_statuses


app = Flask(__name__)
app.register_blueprint(bp_todo)
app.register_blueprint(bp_statuses)
app.register_blueprint(bp_priorities)


@app.errorhandler(404)
def not_found_error_handler(e):
    return jsonify(error=str(e)), 404


@app.route('/')
def index():
    return "Welcome"
