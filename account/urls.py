# _*_ coding:utf-8 _*_
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    # path('login/', views.user_login, name='user_login'), # 自定义登录
    path('login/', auth_views.auth_login, name='user_login'), # django内置登录
    path('new-login/', auth_views.auth_login, {'template_name': 'account/login.html'}, name='user_login'),
]
