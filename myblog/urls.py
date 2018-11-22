# _*_ coding:utf-8 _*_
from django.urls import path
from . import views

app_name = 'myblog'

urlpatterns = [
    path('', views.blog_title, name='blog_title'),
]
