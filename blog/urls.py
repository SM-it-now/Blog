from django.urls import path, include
from . import views

# rest framework
# generic APIView
# from .views import PostListApi, PostDetailApi, PostCreateApi, CategoryListApi, TagListApi, CommentApiView
# viewsets
from .views import PostViewSet
from rest_framework.routers import DefaultRouter

# 각 앱의 url를 구분하기 위해 name을 지정.
app_name = 'blog'

router = DefaultRouter()
router.register(r'post', PostViewSet)

urlpatterns = [
    # path('', views.PostList.as_view(), name='list'),
    # path('create_post/', views.PostCreate.as_view(), name='create_post'),
    # path('<int:pk>/', views.PostDetail.as_view(), name='detail'),
    # path('<int:pk>/new_comment/', views.new_comment, name='new_comment'),
    # path('category/<str:slug>/', views.category_page, name='category_page'),
    # path('tag/<str:slug>/', views.tag_page, name='tag_page'),
    # path('update_post/<int:pk>/', views.PostUpdate.as_view(), name='update_post'),

    # rest framework
    # viewsets
    path('', include(router.urls))

    # # generic APIView
    # path('api/post/', PostListApi.as_view(), name='post_list_api'),
    # path('api/post/category/<str:slug>/', CategoryListApi.as_view()),
    # path('api/post/tag/<str:slug>/', TagListApi.as_view()),
    # path('api/post/<int:pk>/', PostDetailApi.as_view(), name='post_detail_api'),
    # path('api/post/comment/', CommentApiView.as_view()),
    # path('api/post/create/', PostCreateApi.as_view()),
]