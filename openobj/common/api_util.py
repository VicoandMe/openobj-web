import json
import re
from django.http import HttpResponse
from django.utils.html import conditional_escape


def trans_illegal(s):
    """
    转换不合法的字符
    """
    g = lambda src: src if re.search(r'^http', src) else conditional_escape(src)
    if isinstance(s, str):
        return g(s)
    elif isinstance(s, (list, tuple)):
        s = list(s)
        for i in s:
            trans_illegal(i)
    elif isinstance(s, dict):
        for k, v in s.items():
            s[k] = trans_illegal(v)
    else:
        pass
    return s


def http_response_json(status=0, msg="", data=""):
    data = trans_illegal(data)
    return HttpResponse(content=json.dumps({'status': status, 'msg': msg, 'data': data}),
                        content_type="application/json")