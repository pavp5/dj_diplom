from rest_framework import serializers


from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # representation['comments'] = Comment.objects.filter(id__in=instance.comments.all()).values()
        representation['comments'] = CommentSerializer(instance.comments, many=True).data
        return representation
