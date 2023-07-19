from django.contrib import admin
from .models import Category, Keyword, Meme, User, Comment, Like, Share, GeneratedMeme

admin.site.register(Category)
admin.site.register(Keyword)
admin.site.register(Meme)
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Share)
admin.site.register(GeneratedMeme)
