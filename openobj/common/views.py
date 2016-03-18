from django.shortcuts import render, render_to_response
from django.http import HttpResponse


#首页
def index_page(request):
    """
    打开首页
    """
    return render_to_response('common/index.html')