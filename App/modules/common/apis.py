from flask_restful import Resource
from flask import Response


class CommonText(Resource):
    @staticmethod
    def get():
        return Response('测试第二种拆分结构')
