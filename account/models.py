from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True,verbose_name='用户名')
    birth = models.DateField(blank=True, null=True,verbose_name='生日')
    phone = models.CharField(max_length=20, null=True,verbose_name='手机号码')

    def __str__(self):
        return 'user{}'.format(self.user.username)
