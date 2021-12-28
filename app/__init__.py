import os
from flask import Flask


def _initialize_blueprints(app) -> None:
    from app.routes.home import home
    app.register_blueprint(home)


def create_app() -> Flask:
    app = Flask(__name__, template_folder='templates', static_folder='static')
    _initialize_blueprints(app)
    return app