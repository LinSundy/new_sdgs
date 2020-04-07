from flask import session, Response


def init_views(module):
    @module.route('/views/')
    def views_login():
        username = session.get('username')
        return Response('你好，%s' % username)
