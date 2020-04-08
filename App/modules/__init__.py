from .common import common
from .login import login
from flask_sqlalchemy import SQLAlchemy
import os
API = os.environ.get('API_URL')
db = SQLAlchemy()


def init_register_blueprint(app):
    app.register_blueprint(common)
    app.register_blueprint(login)


def init_db(app):
    db.init_app(app)
