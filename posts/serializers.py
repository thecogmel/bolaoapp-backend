from dataclasses import field
from pyexpat import model
from rest_framework import serializers

from accounts.serializers import UserSerializer
from .models import Post, Reaction


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    reactions = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            "id",
            "content",
            "description",
            "user",
            "reactions",
            "created_at",
            "modified_at",
        )

    def get_reactions(self, obj):
        all_reactions = Reaction.objects.filter(post__id=obj.id)
        return ReactionSerializer(all_reactions, many=True).data


class ReactionSerializer(serializers.ModelSerializer):
    """user = UserSerializer(read_only=True)"""

    """ post = PostSerializer() """

    class Meta:
        model = Reaction
        fields = ("id", "like", "user", "post", "created_at", "modified_at")


class ListReactionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Reaction
        fields = ("id", "like", "user", "post", "created_at", "modified_at")
