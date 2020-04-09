from flask import Flask
from .modules import init_register_blueprint
from .ext import init_ext
from datetime import timedelta
from flask_cors import CORS
import os


def create_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    app.config['JSON_AS_ASCII'] = False
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=60 * 2)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:devLGM123@39.100.101.91/new_sdgs'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
    init_ext(app)
    init_register_blueprint(app)
    return app
