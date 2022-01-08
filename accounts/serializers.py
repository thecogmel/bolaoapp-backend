from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "name",
            "nickname",
            "password",
        )
        extra_kwargs = {
            "password": {"write_only": True, "min_length": 6, "required": True},
            "name": {"required": True},
        }

    def create(self, validated_data):
        """Create User - Promoter and competitor by default"""
        user = User.objects.create_user(**validated_data)

        user.save()

        #        """Send verification email to the user"""
        #        token = RefreshToken.for_user(user).access_token

        #        Util.send_email(data=email_data)

        return user


class SearchUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "name", "nickname")


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    name = serializers.CharField(max_length=60, read_only=True)
    nickname = serializers.CharField(max_length=60, read_only=True)

    class Meta:
        fields = (
            "email",
            "password",
            "name",
            "nickname",
        )
        extra_kwargs = {
            "password": {"write_only": True},
            "name": {"read_only": True},
        }
