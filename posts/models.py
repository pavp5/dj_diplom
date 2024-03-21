from django.db import models
# from django.db.models.functions import Now
from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):
    text = models.TextField(max_length=200, default='')
    image = models.ImageField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)



# для доп. задания
# class PostImage(models.Model):
#     ...


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='like')


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=200)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


