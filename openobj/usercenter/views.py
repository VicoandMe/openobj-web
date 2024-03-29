from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import ensure_csrf_cookie
from common import response_helper
from . import logic


@ensure_csrf_cookie
def register(request):
    """
    注册
    :param request:
    """
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        status, msg = logic.register(request, username, email, password)
        return response_helper.http_response_json(status, msg, {})
    else:
        return render(request, 'usercenter/register.html', {})


@ensure_csrf_cookie
def register_success(request):
    """
    打开注册成功页面
    :param request:
    :return:
    """
    return response_helper.render_response_html(request, 'usercenter/register_success.html', {})


@ensure_csrf_cookie
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
        if request.session.get('guid'):
            return HttpResponseRedirect('/')
        else:
            return render_to_response('usercenter/login.html')


@ensure_csrf_cookie
def logout(request):
    """
    登出
    """
    if request.session.get('guid'):
        del request.session['guid']
    return HttpResponseRedirect('/')


@ensure_csrf_cookie
def verify_email_code(request):
    if request.method == "POST":
        code = request.POST.get("code")
        status, msg = logic.verify_register_email(code)
        return response_helper.http_response_json(status, msg, {})


@ensure_csrf_cookie
def user_index(request):
    """
    个人首页
    """
    if request.method == "POST":
        pass
    else:
        if not request.session.get('guid'):
            return HttpResponseRedirect('/')
        else:
            return response_helper.render_response_html(request, 'usercenter/user_index.html', {})


@ensure_csrf_cookie
def user_info(request):
    """
    个人资料
    """
    user_guid = request.session.get('guid')
    if request.method == "POST":
        nick_name = request.POST.get("nick_name")
        user_sex = request.POST.get("sex")
        user_bir = request.POST.get("birthday")
        status, msg = logic.save_userinfo(user_guid,nick_name, user_sex, user_bir)
        return response_helper.http_response_json(status, msg, {})
    else:
        if not user_guid:
            return HttpResponseRedirect('/')
        else:
            data = logic.get_user_info(user_guid)
            return response_helper.render_response_html(request, 'usercenter/user_info.html', data)


@ensure_csrf_cookie
def user_account(request):
    """
    账户设置
    """
    user_guid = request.session.get('guid')
    if not user_guid:
        return HttpResponseRedirect('/')

    if request.method == "POST":
        old_password = request.POST.get("old_pwd")
        new_password = request.POST.get("new_pwd")
        status, msg = logic.change_password(user_guid, old_password, new_password)
        return response_helper.http_response_json(status, msg, {})
    else:
        data = logic.get_user_account(user_guid)
        return response_helper.render_response_html(request, 'usercenter/user_account.html', data)


