import json

from flask_restful import Resource, reqparse, marshal, fields
from App.utils import handle_error, handle_data, login_required
from flask import session, g
from .models import SysUser
import uuid

parser = reqparse.RequestParser()
parser.add_argument('username', type=str)
parser.add_argument('password', type=str)


class Login(Resource):
    @staticmethod
    def get():
        user = SysUser.query.get(1)
        return user.phone

    @staticmethod
    def post():
        # 登陆
        args = parser.parse_args()
        username = args.get('username')
        password = args.get('password')
        if not username:
            return handle_error(20001, 'username')
        if not password:
            return handle_error(20001, 'password')

        user = SysUser.query.filter(SysUser.username == username).first()

        if not user:
            return handle_data(False, msg='用户不存在！')
        if password != user.password:
            return handle_data(False, msg='用户名密码不正确！')
        token = str(uuid.uuid1())
        info = {
            'token': token,
            'user_id': user.id
        }
        session['Authorization'] = json.dumps(info)
        return handle_data(info)


class RoleStr(fields.Raw):
    def format(self, value):
        return value.name


class User(Resource):
    @login_required
    def get(self):
        # 获取用户信息
        role_fields = {
            'id': fields.Integer,
            'name': fields.String
        }
        user_fields = {
            'id': fields.Integer,
            'username': fields.String,
            'password': fields.String,
            'avatar': fields.String,
            'name': fields.String,
            'roles': fields.List(RoleStr(role_fields))
        }
        user = g.user
        data = marshal(user, user_fields)
        return handle_data(data)


class LogOut(Resource):
    @staticmethod
    def post():
        # 登出
        session.pop("Authorization", None)
        return handle_data('')
