from django.urls import path
from .views import (
    CategoryListAPIView,
    CategoryDetailAPIView,
    KeywordListAPIView,
    KeywordDetailAPIView,
    MemeListAPIView,
    MemeDetailAPIView,
    UserListAPIView,
    UserDetailAPIView,
    CommentListAPIView,
    CommentDetailAPIView,
    LikeListAPIView,
    LikeDetailAPIView,
    ShareListAPIView,
    ShareDetailAPIView,
    GeneratedMemeListAPIView,
    GeneratedMemeDetailAPIView,
)

urlpatterns = [
    # ...
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('keywords/', KeywordListAPIView.as_view(), name='keyword-list'),
    path('keywords/<int:pk>/', KeywordDetailAPIView.as_view(), name='keyword-detail'),
    path('memes/', MemeListAPIView.as_view(), name='meme-list'),
    path('memes/<int:pk>/', MemeDetailAPIView.as_view(), name='meme-detail'),
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('comments/', CommentListAPIView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetailAPIView.as_view(), name='comment-detail'),
    path('likes/', LikeListAPIView.as_view(), name='like-list'),
    path('likes/<int:pk>/', LikeDetailAPIView.as_view(), name='like-detail'),
    path('shares/', ShareListAPIView.as_view(), name='share-list'),
    path('shares/<int:pk>/', ShareDetailAPIView.as_view(), name='share-detail'),
    path('generated-memes/', GeneratedMemeListAPIView.as_view(), name='generated-meme-list'),
    path('generated-memes/<int:pk>/', GeneratedMemeDetailAPIView.as_view(), name='generated-meme-detail'),
    # ...
]
