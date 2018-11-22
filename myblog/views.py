from django.shortcuts import render
from .models import BlogArticles


# Create your views here.


def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request, 'myblog/titles.html', locals())
