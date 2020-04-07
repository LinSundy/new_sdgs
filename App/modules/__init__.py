from .common import common
from .login import login
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def init_register_blueprint(app):
    app.register_blueprint(common, url_prefix='/common')
    app.register_blueprint(login, url_prefix='/login')


def init_db(app):
    db.init_app(app)
