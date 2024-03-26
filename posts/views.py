from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from posts.models import Post, Comment
from posts.serializers import PostSerializer, CommentSerializer

# Create your views here.
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer