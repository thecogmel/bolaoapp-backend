from django.urls import path
from django.conf.urls import include

from rest_framework.routers import DefaultRouter
from .views import PostViewSet, ReactionViewSet

router = DefaultRouter()

router.register("post", PostViewSet, basename="post")
router.register("reaction", ReactionViewSet, basename="reaction")

urlpatterns = [
    path("", include(router.urls)),
]
