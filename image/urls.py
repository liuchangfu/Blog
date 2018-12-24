# _*_ coding:utf-8 _*_
from django.conf.urls import url
from . import views
from django.urls import path, re_path

app_name = 'image'

urlpatterns = [
    path('list-images/', views.list_images, name='list_images'),
    path('upload-images/', views.upload_image, name='upload_image'),
    path('del-images/', views.del_image, name='del_image'),
    path('images/', views.falls_images, name='falls_images'),
]
