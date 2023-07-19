from rest_framework import serializers
from .models import Category, Keyword, Meme, User, Comment, Like, Share, GeneratedMeme


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = '__all__'


class MemeSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    keywords = KeywordSerializer(many=True)

    class Meta:
        model = Meme
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Like
        fields = '__all__'


class ShareSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Share
        fields = '__all__'


class GeneratedMemeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = GeneratedMeme
        fields = '__all__'
