from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie

from . import response_helper


@ensure_csrf_cookie
def index_page(request):
    """
    打开首页
    """
    return response_helper.render_response_html(request,'common/index.html', {})