from flask_restful import Resource, reqparse
from App.utils import handle_error
from .models import SysUser

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
        return '登陆'
