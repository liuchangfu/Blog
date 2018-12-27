from django.db import models
from django.contrib.auth.models import User
from slugify import slugify


# Create your models here.

class Course(models.Model):
    user = models.ForeignKey(User, related_name='courses_user', on_delete=models.CASCADE, verbose_name='作者')
    title = models.CharField(max_length=200, verbose_name='标题')
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField(verbose_name='概述')
    created = models.DateField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        ordering = ('-created',)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
