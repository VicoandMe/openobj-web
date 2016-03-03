from django.shortcuts import render

# Create your views here.

def register(request):
    """
    注册
    """
    account = request.POST.get("account")
    password = request.POST.get("password")
