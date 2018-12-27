# _*_ coding:utf-8 _*_
from django import forms
from .models import Course


class CreateCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'overview')
