from flask import Flask
from flask import jsonify

from .routes.tasks import todo
from .routes.status import statuses


app = Flask(__name__)
app.register_blueprint(todo)
app.register_blueprint(statuses)


@app.errorhandler(404)
def not_found_error_handler(e):
    return jsonify(error=str(e)), 404


@app.route('/')
def index():
    return "Welcome"
