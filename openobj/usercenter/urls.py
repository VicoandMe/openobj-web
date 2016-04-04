from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register/success/$', views.register_success, name='register_success'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^email/verify/$', views.verify_email_code, name='verify_email_code'),
    url(r'^user_info/$',views.passwordsave,name='user_info'),
]