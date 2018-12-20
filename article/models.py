from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from slugify import slugify
from django.urls import reverse


# Create your models here.

class ArticleColumn(models.Model):
    user = models.ForeignKey(User, related_name='article_column', on_delete=models.CASCADE, verbose_name='用户')
    column = models.CharField(max_length=200, verbose_name='列')
    created = models.DateField(auto_now_add=True, verbose_name='创建日期')

    def __str__(self):
        return self.column

    class Meta:
        verbose_name_plural = '文章列表'
        verbose_name = '文章列表'


class ArticleTag(models.Model):
    author = models.ForeignKey(User, related_name='tag', on_delete=models.CASCADE, verbose_name='作者')
    tag = models.CharField(max_length=500, verbose_name='标签')

    def __str__(self):
        return self.tag


class ArticlePost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article', verbose_name='作者')
    title = models.CharField(max_length=200, verbose_name='标题')
    slug = models.SlugField(max_length=500)
    column = models.ForeignKey(ArticleColumn, related_name='article_column', on_delete=models.CASCADE, verbose_name='列')
    body = models.TextField(verbose_name='正文')
    created = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    users_like = models.ManyToManyField(User, related_name='article_like', blank=True, verbose_name='点赞数')
    article_tag = models.ManyToManyField(ArticleTag, related_name='article_tag', blank=True)

    class Meta:
        ordering = ('-updated',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(ArticlePost, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('article:article_detail', args=[self.id, self.slug])

    def get_url_path(self):
        return reverse('article:list_article_detail', args=[self.id, self.slug])


class Comment(models.Model):
    article = models.ForeignKey(ArticlePost, related_name='comments', on_delete=models.CASCADE, verbose_name='文章')
    commentator = models.CharField(max_length=90, verbose_name='评论员')
    body = models.TextField(verbose_name='正文')
    created = models.DateTimeField(auto_now=True, verbose_name='创建者')

    class Meta():
        ordering = ('-created',)

    def __str__(self):
        return 'Comment by {0} on {1}'.format(self.commentator.username, self.article)
