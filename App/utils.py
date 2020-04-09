def handle_error(code, name='', **kwargs):
    res = {
        "code": code,
        "data": None,
        "msg": ''
    }
    if code == 20001:
        res['msg'] = '%s 参数不能为空' % name
    if code == 20000:
        res['msg'] = kwargs.get('msg')
    return res


def handle_data(data):
    res = {
        "code": 20000,
        "data": data,
        "msg": 'ok'
    }
    return res
