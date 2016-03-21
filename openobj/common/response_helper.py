import json
from libs import api_util
from django.http import HttpResponse
from django.shortcuts import render
from usercenter.models import UserAccount


def http_response_json(status=0, msg="", data=""):
    """
    http返回json数据
    """
    data = api_util.trans_illegal(data)
    return HttpResponse(content=json.dumps({'status': status, 'msg': msg, 'data': data}),
                        content_type="application/json")


def render_response_html(request, html, data):
    guid = request.session.get("guid")
    try:
        user = UserAccount.objects.get(guid=guid)
        data["username"] = user.user_name
    except UserAccount.DoesNotExist:
        pass
    return render(request, html, data)