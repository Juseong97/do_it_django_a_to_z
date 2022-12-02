# from django.shortcuts import render //FBV
from django.views.generic import ListView, DetailView
from .models import Post, Category



class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

    # template_name = 'blog/post_list.html' 방법 1 새로안만들고 템플릿 명 명시하기.

class PostDetail(DetailView):
    model = Post


# FBV로 만들기 (함수형)
# def single_post_page(request, pk):
#     post=Post.objects.get(pk=pk)
#
#     return render(
#         request,
#         'blog/post_detail.html',
#         {
#             'post':post,
#         }
#
#     )

# def index(request):
#     posts=Post.objects.all().order_by('-pk')
#     return render(
#         request,
#         'blog/post_list.html',
#         {
#             'posts':posts,
#         }
#     )
