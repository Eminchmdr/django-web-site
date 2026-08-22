from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Blog, Category


def index(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True, is_home=True),
        "categories": Category.objects.all()
    }
    return render(request, 'index.html', context)


def blogs(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True),
        "categories": Category.objects.all()
    }
    return render(request, 'blogs.html', context)


def blogs_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, 'blogs-details.html', {
        "blog": blog
    })


def blogs_by_category(request, slug):
    pass
