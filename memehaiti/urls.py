from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

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

    #Swagger**********************
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # ...
]
