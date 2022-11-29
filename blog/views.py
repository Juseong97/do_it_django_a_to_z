from django.shortcuts import render
from .models import Post

def index(requset):
    posts=Post.objects.all().order_by('-pk')
    return render(
        requset,
        'blog/index.html',
        {
            'posts':posts,
        }
    )
