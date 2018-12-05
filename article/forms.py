# _*_ coding:utf-8 _*_
from django import forms
from .models import ArticleColumn, ArticelPost


class ArticleColumnForm(forms.ModelForm):
    class Meta:
        model = ArticleColumn
        fields = ('column',)


class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = ArticelPost
        fields = ('title','body')
