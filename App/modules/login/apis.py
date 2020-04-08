from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('username', required=True, type=str, help='用户名不能为空')
parser.add_argument('password', required=True, type=str, help='密码不能为空')


class Login(Resource):
    @staticmethod
    def post():
        args = parser.parse_args()
        username = args.get('username')
        password = args.get('password')
        print(username, password, '参数')
