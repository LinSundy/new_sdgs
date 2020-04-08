from flask import Flask
from .modules import init_register_blueprint, init_db
from datetime import timedelta
import os


def create_app():
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=60 * 2)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:devLGM123@39.100.101.91/new_sdgs'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
    init_register_blueprint(app)
    init_db(app)
    return app
