from flask import Flask
from .modules import init_register_blueprint
from datetime import timedelta
import os


def create_app():
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=60 * 2)
    app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
    init_register_blueprint(app)
    return app
