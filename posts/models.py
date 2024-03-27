from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(null=True)
    # image = models.ImageField(null=True)
    # Поле для ввода и отображения месторасположения объекта
    address = models.TextField(null=True)
    latitude = models.DecimalField(null=True, max_digits=8, decimal_places=6)
    longtitude = models.DecimalField(null=True, max_digits=8, decimal_places=6)
    like_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)



# для доп. задания
class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField()



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


