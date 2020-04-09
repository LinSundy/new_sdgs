from flask_restful import Resource, reqparse
from App.utils import handle_error, handle_data
from flask import session, jsonify
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
        args = parser.parse_args()
        username = args.get('username')
        password = args.get('password')
        if not username:
            return handle_error(20001, 'username')
        if not password:
            return handle_error(20001, 'password')

        user = SysUser.query.filter(SysUser.username == username).first()

        if not user:
            return handle_error(20000, msg='用户不存在！')
        if password != user.password:
            return handle_error(20000, msg='用户名密码不正确！')
        token = str(uuid.uuid1())
        session['Authorization'] = token
        return handle_data(token)
