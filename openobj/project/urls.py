from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.find_project_page),
    url(r'^info/', views.project_info),
]