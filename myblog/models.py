from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class BlogArticles(models.Model):
    title = models.CharField(max_length=300, verbose_name='标题')
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE, verbose_name='发布人')
    body = models.TextField(verbose_name='正文')
    publish = models.DateTimeField(default=timezone.now, verbose_name='发布时间')

    class Meta:
        ordering = ('-publish',)
        verbose_name_plural = '博客文章'

    def __str__(self):
        return self.title
