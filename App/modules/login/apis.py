from flask_restful import Resource, reqparse
from App.utils import handle_error
parser = reqparse.RequestParser()
parser.add_argument('username', type=str)
parser.add_argument('password', type=str)


class Login(Resource):
    @staticmethod
    def post():
        args = parser.parse_args()
        username = args.get('username')
        password = args.get('password')
        if not username:
            return handle_error(20001, 'username')
        if not password:
            return handle_error(20001, 'password')
