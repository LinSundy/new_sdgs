from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate(compare_type=True)


def init_ext(app):
    db.init_app(app)
    migrate.init_app(app, db)
