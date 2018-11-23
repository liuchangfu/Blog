# _*_ coding:utf-8 _*_
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth.views import LoginView

app_name = 'account'

urlpatterns = [
    # path('login/', views.user_login, name='user_login'), # 自定义登录
    path('login/', LoginView.as_view(), name='user_login'),  # django内置登录
    path('new-login/', LoginView.as_view(), {'template_name': 'account/login.html'}, name='user_login'),
]
