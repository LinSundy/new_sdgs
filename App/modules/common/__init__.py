from flask import Blueprint, Response
from flask_restful import Api
from .apis import CommonText
from .views import init_view


common = Blueprint('common', __name__)
api = Api(common)

api.add_resource(CommonText, '/demo/')


init_view(common)

# @common.route('/a/')
# def a():
#     return Response('啊啊啊啊')



