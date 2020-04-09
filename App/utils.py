def handle_error(code, name=''):
    res = {
        "code": code,
        "data": None,
        "msg": ''
    }
    if code == 20001:
        res['msg'] = '%s 参数不能为空' % name
    return res
