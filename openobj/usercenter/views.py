from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from . import logic
from common import api_util


@csrf_exempt
def register(request):
    """
    注册
    :param request:
    """
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        status, msg = logic.register(username, email, password)
        return api_util.http_response_json(status, msg, {})
    else:
        return render(request, 'usercenter/register.html', {})


def register_success(request):
    """
    打开注册成功页面
    :param request:
    :return:
    """
    return render(request, 'usercenter/register_success.html', {})


def login(request):
    """
    打开登录页面
    """
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        status, msg = logic.login(email, password)
        return api_util.http_response_json(status, msg, {})
    else:
        return render_to_response('usercenter/login.html')