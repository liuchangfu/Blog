from django.db import models
from django.contrib.auth.models import User
from slugify import slugify
from .fields import OrderField


# Create your models here.

class Course(models.Model):
    user = models.ForeignKey(User, related_name='courses_user', on_delete=models.CASCADE, verbose_name='作者')
    title = models.CharField(max_length=200, verbose_name='标题')
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField(verbose_name='概述')
    created = models.DateField(auto_now_add=True, verbose_name='创建时间')
    student = models.ManyToManyField(User, related_name='courses_joined', blank=True, verbose_name='学生')

    class Meta:
        ordering = ('-created',)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


def user_directory_path(instance, filename):
    return 'course/user_{0}/{1}'.format(instance.user.id, filename)


class Lesson(models.Model):
    user = models.ForeignKey(User, related_name='lesson_user', on_delete=models.CASCADE, verbose_name='用户')
    course = models.ForeignKey(Course, related_name='lesson', on_delete=models.CASCADE, verbose_name='课程')
    title = models.CharField(max_length=200, verbose_name='标题')
    video = models.FileField(upload_to=user_directory_path, verbose_name='视频')
    description = models.TextField(blank=True, verbose_name='描述')
    attach = models.FileField(blank=True, upload_to=user_directory_path, verbose_name='附件')
    created = models.DateField(auto_now_add=True, verbose_name='创建人')
    order = OrderField(blank=True, for_fields=['course'])

    class Meta:
        ordering = ['order']

    def __str__(self):
        return '{}.{}'.format(self.order, self.title)
