"""
URL configuration for social_network project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from posts.views import PostViewSet, LikeViewSet, CommentViewSet, PostImageViewSet

post_router = DefaultRouter()
post_router.register("posts", PostViewSet, basename="posts")

comment_router = DefaultRouter()
comment_router.register("comments", CommentViewSet, basename="comments")

image_router = DefaultRouter()
image_router.register("images", PostImageViewSet, basename="images")

like_router = DefaultRouter()
like_router.register("likes", LikeViewSet, basename="likes")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(post_router.urls)),
    path("api/", include(comment_router.urls)),
    path("api/", include(image_router.urls)),
    path("api/", include(like_router.urls)),

]
