from rest_framework import serializers
from geopy.geocoders import Nominatim

from .models import Post, Comment, PostImage

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ["user", ]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ["user", "latitude", "longtitude", ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["images"] = PostImageSerializer(instance.images, many=True).data
        representation["comments"] = CommentSerializer(instance.comments, many=True).data
        # Определение адреса по геогрфичеким координатам
        if representation["latitude"] is not None:
            geolocator = Nominatim(user_agent="social_network")
            location = geolocator.reverse(f"{representation["latitude"]}, {representation["longtitude"]}")
            representation["address"] = location.address
        return representation


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = "__all__"
