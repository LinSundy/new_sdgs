import os

from .common import common
from .login import login
from .company import company
# API_URL = os.environ.get('API_URL') or '/sdas-api'
API_URL = '/sdgs-api'


def init_register_blueprint(app):
    app.register_blueprint(common, url_prefix=API_URL)
    app.register_blueprint(login, url_prefix=API_URL)
    app.register_blueprint(company, url_prefix=API_URL)
