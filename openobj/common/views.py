from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index_page(request):
    """
    打开首页
    """
    return render(request, 'common/index.html', {})