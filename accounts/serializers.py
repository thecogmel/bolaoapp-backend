from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "name",
            "nickname",
            "password",
        )
        extra_kwargs = {
            "password": {"write_only": True, "min_length": 6, "required": True},
            "nickname": {"required": True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        user.save()

        return user


class SearchUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "name", "nickname")


class LoginSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    name = serializers.CharField(max_length=60, read_only=True)
    nickname = serializers.CharField(max_length=60)

    class Meta:
        fields = (
            "password",
            "name",
            "nickname",
        )
        extra_kwargs = {
            "password": {"write_only": True},
            "nickname": {"read_only": True},
        }
