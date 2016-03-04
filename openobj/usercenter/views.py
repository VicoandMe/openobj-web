from django.shortcuts import render, render_to_response

# Create your views here.

def register(request):
    """
    注册
    """
    account = request.POST.get("account")
    password = request.POST.get("password")


def login(request):
    return render_to_response('usercenter/login.html')
