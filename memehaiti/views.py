from django.shortcuts import render
from rest_framework import generics
from .models import Category, Keyword, Meme, User, Comment, Like, Share, GeneratedMeme
from .serializers import (
    CategorySerializer,
    KeywordSerializer,
    MemeSerializer,
    UserSerializer,
    CommentSerializer,
    LikeSerializer,
    ShareSerializer,
    GeneratedMemeSerializer,
)


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class KeywordListAPIView(generics.ListAPIView):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer


class KeywordDetailAPIView(generics.RetrieveAPIView):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer


class MemeListAPIView(generics.ListAPIView):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer


class MemeDetailAPIView(generics.RetrieveAPIView):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CommentListAPIView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetailAPIView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class LikeListAPIView(generics.ListAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class LikeDetailAPIView(generics.RetrieveAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class ShareListAPIView(generics.ListAPIView):
    queryset = Share.objects.all()
    serializer_class = ShareSerializer


class ShareDetailAPIView(generics.RetrieveAPIView):
    queryset = Share.objects.all()
    serializer_class = ShareSerializer


class GeneratedMemeListAPIView(generics.ListAPIView):
    queryset = GeneratedMeme.objects.all()
    serializer_class = GeneratedMemeSerializer


class GeneratedMemeDetailAPIView(generics.RetrieveAPIView):
    queryset = GeneratedMeme.objects.all()
    serializer_class = GeneratedMemeSerializer

