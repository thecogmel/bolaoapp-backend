from django.shortcuts import render

from rest_framework import generics, mixins, viewsets, permissions, status

from .serializers import PostSerializer

from .models import Post


# Create your views here.
class PostViewSet(
    viewsets.GenericViewSet,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
