from flask import session, g
import json
from .modules.login.models import SysUser
from flask_restful import reqparse


parser = reqparse.RequestParser()
parser.add_argument('token', type=str)


def handle_error(code, name='', **kwargs):
    res = {
        "code": code,
        "data": None,
        "msg": ''
    }
    if code == 20001:
        res['msg'] = '%s 参数不能为空' % name
    if code == 20000 or code == 50014 or code == 50008:
        res['msg'] = kwargs.get('msg')
    return res


def handle_data(data, **kwargs):
    res = {
        "code": 20000,
        "data": data,
        "msg": "%s" % (kwargs.get('msg') or 'ok')
    }
    return res


def login_required(fun):
    def wrapper(*args):
        if not session.get('Authorization'):
            return handle_error(50014, 'token过期')
        info = json.loads(session.get('Authorization'))
        token = info.get('token')
        user_id = info.get('user_id')
        args = parser.parse_args()
        req_token = args.get('token')
        if token != req_token:
            return handle_error(50008, 'token失效')
        user = SysUser.query.get(user_id)
        g.user = user
        return fun(*args)
    return wrapper
