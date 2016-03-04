from django.shortcuts import render, render_to_response

# Create your views here.


def register_page(request):
    return render_to_response('usercenter/register.html')


def register(request):
    """
    注册
    :param request:
    :return:
    """


def login_page(request):
    return render_to_response('usercenter/login.html')