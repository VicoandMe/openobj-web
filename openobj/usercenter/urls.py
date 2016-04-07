from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register/success/$', views.register_success, name='register_success'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^email/verify/$', views.verify_email_code, name='verify_email_code'),
    url(r'^my/$', views.user_index, name='user_index'),
    url(r'^info/$', views.user_info, name='user_info'),
    url(r'^account/$', views.user_account, name='user_account'),
]