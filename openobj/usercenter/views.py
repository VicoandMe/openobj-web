from django.core.serializers import json
from django.shortcuts import render, render_to_response

# Create your views here.


def register(request):
    """
    注册
    """
    if (request.method == "POST"):
        parameter = request.POST.get("parameter")
        decodejson = json.loads(parameter)
        username = decodejson.get("username")
        email = decodejson.get("email")
        password = decodejson.get("password")
        print(username)
        print(email)
        print(password)
    else:
        return render_to_response('usercenter/register.html')


def login_page(request):
    """
    打开登录页面
    """
    return render_to_response('usercenter/login.html')