# _*_ coding:utf-8 _*_
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeDoneView, PasswordChangeView, \
    PasswordResetView, PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView

app_name = 'account'

urlpatterns = [
    # path('login/', views.user_login, name='user_login'), # 自定义登录
    path('login/', LoginView.as_view(), name='user_login'),  # django内置登录

    path('new-login/', LoginView.as_view(template_name='account/login.html'), name='user_login'),

    path('logout/', LogoutView.as_view(template_name='account/logout.html'), name='user_logout'),

    path('register/', views.register, name='user_register'),

    path('password-change/', PasswordChangeView.as_view(template_name='account/password_change_form.html',
                                                        success_url='/account/password-change-done',
                                                        ), name='password_change'),

    path('password-change-done/', PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'),
         name='password_change_done'),

    path('password-reset/', PasswordResetView.as_view(template_name='account/password_reset_form.html',
                                                      email_template_name='account/password_reset_email.html',
                                                      success_url='/account/password-reset-done',
                                                      subject_template_name='account/password_reset_subject.txt',
                                                      ), name='password_reset'),

    path('password-reset-done/', PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html',
                                          success_url='/account/password-reset-complete'),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
         name='password_reset_complete'),

    path('my-information/', views.myself, name='my_informaiton'),

    path('edit-my-information/', views.myself_edit, name='edit_my_informaiton'),

    path('my-image/', views.my_image, name='my-image'),
]
