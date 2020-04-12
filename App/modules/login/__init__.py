from flask import Blueprint
from flask_restful import Api
from .views import init_views
from .apis import Login, User, LogOut

login = Blueprint('login', __name__)
api = Api(login)
api.add_resource(Login, '/login/')
api.add_resource(User, '/userinfo/')
api.add_resource(LogOut, '/logout/')
init_views(login)



