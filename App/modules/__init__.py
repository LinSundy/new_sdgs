from .common import common
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def init_register_blueprint(app):
    app.register_blueprint(common, url_prefix='/common')


def init_db(app):
    db.init_app(app)
