from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response

from common import response_helper
from libs import api_util
from . import logic


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
        return response_helper.http_response_json(status, msg, {})
    else:
        return render(request, 'usercenter/register.html', {})


def register_success(request):
    """
    打开注册成功页面
    :param request:
    :return:
    """
    return response_helper.render_response_html(request,'usercenter/register_success.html', {})


def login(request):
    """
    打开登录页面
    """
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        status, msg = logic.login(request, email, password)
        return response_helper.http_response_json(status, msg, {})
    else:
        return render_to_response('usercenter/login.html')


def logout(request):
    """
    登出
    """
    if request.session.get('guid'):
        del request.session['guid']
    return HttpResponseRedirect('/')
