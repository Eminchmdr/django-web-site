from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Blog


def index(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True, is_home=True)
    }
    return render(request, 'index.html', context)


def blogs(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True)
    }
    return render(request, 'blogs.html', context)


def blogs_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, 'blogs-details.html', {
        "blog": blog
    })
