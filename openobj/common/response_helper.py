import json
import re

from django.utils.html import conditional_escape
from django.http import HttpResponse
from django.shortcuts import render
from usercenter.models import UserAccount


def trans_illegal(s):
    """
    转换不合法的字符
    :param s:
    :return:
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


def http_response_json(status=0, msg="", data={}):
    """
    http返回json数据
    """
    data = trans_illegal(data)
    return HttpResponse(content=json.dumps({'status': status, 'msg': msg, 'data': data}),
                        content_type="application/json")


def render_response_html(request, html, data={}):
    guid = request.session.get("guid")
    try:
        user = UserAccount.objects.get(guid=guid)
        data["username"] = user.user_name
    except UserAccount.DoesNotExist:
        pass
    return render(request, html, data)