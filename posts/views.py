from django.shortcuts import render

from rest_framework import generics, mixins, viewsets, permissions, status
from rest_framework.response import Response

from .serializers import ListReactionSerializer, PostSerializer, ReactionSerializer

from .models import Post, Reaction


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(
                {"post": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReactionViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Reaction.objects.all()
    serializer_class = ListReactionSerializer

    def create(self, request, *args, **kwargs):
        request.data["user"] = request.user.id
        serializer = ReactionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"reaction": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
