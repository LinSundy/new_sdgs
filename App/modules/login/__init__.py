from flask import Blueprint
from flask_restful import Api
from .views import init_views

from .apis import Login

login = Blueprint('login', __name__)

api = Api(login)
api.add_resource(Login, '/api/')

init_views(login)
