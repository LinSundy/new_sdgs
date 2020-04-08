import os

from .common import common
from .login import login
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
API_URL = os.environ.get('API_URL')


def init_register_blueprint(app):
    app.register_blueprint(common, url_prefix=API_URL)
    app.register_blueprint(login, url_prefix=API_URL)


def init_db(app):
    db.init_app(app)
