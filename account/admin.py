from django.contrib import admin
from .models import UserProfile, UserInfo


# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth', 'phone')
    list_filter = ('phone',)


class UserinfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'school', 'company', 'address', 'aboutme', 'photo', 'profession')
    list_filter = ('school', 'company', 'profession')


admin.site.register(UserProfile, UserProfileAdmin)

admin.site.register(UserInfo, UserinfoAdmin)
