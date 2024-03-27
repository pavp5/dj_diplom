from django.shortcuts import render
# from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from geopy.geocoders import Nominatim

from .models import Post, Comment, PostImage
from .serializers import PostSerializer, CommentSerializer, PostImageSerializer
from .permissions import IsOwnerOrReadOnly


# Create your views here.
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        # Определение географических координат
        if "address" in self.request.data:
            geolocator = Nominatim(user_agent="social_network")
            location = geolocator.geocode(self.request.data["address"])
            serializer.save(user=self.request.user, latitude=location.latitude, longtitude=location.longitude)
        else:
            serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        if "address" in self.request.data:
            geolocator = Nominatim(user_agent="social_network")
            location = geolocator.geocode(self.request.data["address"])
            serializer.save(latitude=location.latitude, longtitude=location.longitude)
        else:
            serializer.save()


class PostImageViewSet(ModelViewSet):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer
    permission_classes = [IsOwnerOrReadOnly]



class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)