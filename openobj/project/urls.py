from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.find_project_page),
    url(r'^classify/', views.project_list_classify),
]