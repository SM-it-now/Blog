from django.urls import path
from . import views

# 각 앱의 url를 구분하기 위해 name을 지정.
app_name = 'blog'

urlpatterns = [
    path('', views.PostList.as_view(), name='list'),
    path('<int:pk>/', views.PostDetail.as_view(), name='detail'),
    path('category/<str:slug>/', views.category_page, name='category_page'),
]