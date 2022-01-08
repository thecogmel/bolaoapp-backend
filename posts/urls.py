from django.urls import path
from django.conf.urls import include

from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()

router.register("post", PostViewSet, basename="post")

urlpatterns = [
    path("", include(router.urls)),
]
