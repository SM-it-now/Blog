from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category


# CBV를 이용한 views 클래스 구현하기.
# Create your views here.

# ListView 라이브러리를 이용해서 post 목록을 구현
class PostList(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context


# DetailView 라이브러리를 이용해서 post 상세화면 구현
class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

# 카테고리 별 페이지
def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)
    context = {
        'category': category,
        'post_list': post_list,
        'categories': Category.objects.all(),
        'no_category_post_count': Post.objects.filter(category=None).count()
    }

    return render(request, 'blog/post_list.html', context)

