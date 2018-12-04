# _*_ coding:utf-8 _*_
from django import forms
from .models import ArticleColumn


class ArticleColumnForm(forms.ModelForm):
    class Meta:
        model = ArticleColumn
        fields = ('column',)
