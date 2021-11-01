from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# CBV를 이용한 views 클래스 구현하기.
# Create your views here.

# ListView 라이브러리를 이용해서 post 목록을 구현
class PostList(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    ordering = '-pk'

# DetailView 라이브러리를 이용해서 post 상세화면 구현
class PostDetail(DetailView):
    model = Post
