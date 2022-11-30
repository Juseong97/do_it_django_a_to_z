from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


class PostList(ListView):
    model = Post
    ordering = '-pk'

    # template_name = 'blog/post_list.html' 방법 1 새로안만들고 템플릿 명 명시하기.





def single_post_page(request, pk):
    post=Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post':post,
        }

    )

# def index(request):
#     posts=Post.objects.all().order_by('-pk')
#     return render(
#         request,
#         'blog/post_list.html',
#         {
#             'posts':posts,
#         }
#     )
