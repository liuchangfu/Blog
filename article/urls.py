# _*_ coding:utf-8 _*_
from django.urls import path, re_path
from . import views

app_name = 'article'

urlpatterns = [
    path('article-column/', views.article_column, name='article_column'),
    path('rename-column/', views.rename_article_column, name='rename_article_column'),
    path('del-column/', views.del_article_column, name='del_article_column'),
    path('article-post/', views.article_post, name='article_post'),
    path('article-list/', views.article_list, name='article_list'),
    re_path(r'^article-detail/(?P<id>\d)/(?P<slug>[-\w]+)/$', views.article_detail, name="article_detail"),
    # path('article-detail/<int:id>/<slug:slug>/', views.article_detail, name="article_detail"),
    path('del-article/', views.article_del, name="article_del"),
    path('redit-article/<int:article_id>/', views.redit_article, name="redit_article"),
]
