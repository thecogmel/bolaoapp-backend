from django.urls import path
from django.conf.urls import include

from rest_framework.routers import DefaultRouter
from .views import LoginView, SearchUserListView, UserViewSet

router = DefaultRouter()

router.register("user", UserViewSet, basename="user")


urlpatterns = [
    path("", include(router.urls)),
    path("signin/", LoginView.as_view(), name="signin"),
    path("search-user/", SearchUserListView.as_view(), name="search-user"),
]
