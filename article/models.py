from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class ArticleColumn(models.Model):
    user = models.ForeignKey(User, related_name='articel_column', on_delete=models.CASCADE, verbose_name='用户')
    column = models.CharField(max_length=200, verbose_name='列')
    created = models.DateField(auto_now_add=True, verbose_name='创建日期')

    def __str__(self):
        return self.column

    class Meta:
        verbose_name_plural = '文章列表'
