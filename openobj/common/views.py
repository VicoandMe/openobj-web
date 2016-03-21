from django.shortcuts import render
from . import response_helper


def index_page(request):
    """
    打开首页
    """
    return response_helper.render_response_html(request,'common/index.html', {})