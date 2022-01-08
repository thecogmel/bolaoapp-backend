from rest_framework import serializers

from accounts.serializers import UserSerializer
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ("id", "content", "description", "user")
