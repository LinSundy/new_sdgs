import os

from .common import common
from .login import login
API_URL = os.environ.get('API_URL')


def init_register_blueprint(app):
    app.register_blueprint(common, url_prefix=API_URL)
    app.register_blueprint(login, url_prefix=API_URL)
