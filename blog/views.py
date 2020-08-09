from django.shortcuts import render
from .models import Post


def home(request):
    return render(request, 'blog/home.html')

def blog(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/blog.html', context)

def notice(request):
    return render(request, 'blog/notice.html')

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def read_more(request,id):
    context = {
        'blog': Post.objects.get(pk=id)
    }
    return render(request, 'blog/read_more.html', context)