from django.core.serializers import json
from django.shortcuts import render, render_to_response

# Create your views here.


def register_page(request):
    """
    打开注册页面
    """
    return render_to_response('usercenter/register.html')


def register(request):
    """
    注册
    """
    parameter = request.POST.get("parameter")
    decodejson = json.loads(parameter)
    email = decodejson.get("email")
    password = decodejson.get("password")
    nickname = decodejson.get("nickname")


def login_page(request):
    """
    打开登录页面
    """
    return render_to_response('usercenter/login.html')