def listdatas(pathin, string):
    import os
    _a = []
    _datas = os.listdir(pathin)
    for _i in _datas:
        if _i.endswith(string):
            _fn_i = pathin + '/' + _i
            _a.append(_fn_i)
    return _a