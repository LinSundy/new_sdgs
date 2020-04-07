from flask import Response, session
from flask_restful import Resource


class Login(Resource):
    @staticmethod
    def get():
        session['username'] = 'chelin'
        session.permanent = True
        return Response('登录成功!')
