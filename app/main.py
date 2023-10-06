from flask import Flask

from .routes.tasks import todo


app = Flask(__name__)
app.register_blueprint(todo)


@app.route('/')
def index():
    return "Welcome"

