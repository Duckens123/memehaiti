from .meme_views import MemeListAPIView, MemeDetailAPIView
from .user_views import UserListAPIView, UserDetailAPIView
from .category_views import CategoryListAPIView, CategoryDetailAPIView
from .comment_views import CommentListAPIView, CommentDetailAPIView
from .generatedmeme_views import GeneratedMemeListAPIView, GeneratedMemeDetailAPIView
from .keyword_views import KeywordListAPIView, KeywordDetailAPIView
from .share_views import ShareListAPIView, ShareDetailAPIView
from .like_views import LikeListAPIView,LikeDetailAPIView
__all__ = [
    'MemeListAPIView',
    'MemeDetailAPIView',
    'UserListAPIView',
    'UserDetailAPIView',
    'CategoryListAPIView',
    'CategoryDetailAPIView',
    'CommentListAPIView',
    'CommentDetailAPIView',
    'GeneratedMemeListAPIView',
    'GeneratedMemeDetailAPIView',
    'KeywordListAPIView',
    'KeywordDetailAPIView',
    'ShareListAPIView',
    'ShareDetailAPIView',
    'LikeListAPIView',
    'LikeDetailAPIView'
]