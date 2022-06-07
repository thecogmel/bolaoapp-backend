from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

User = get_user_model()

import uuid

from django.utils import timezone
from rest_framework import generics, mixins, viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .serializers import (
    LoginSerializer,
    ResetPasswordSerializer,
    SearchUserSerializer,
    UserSerializer,
)
from rest_framework import filters
from .models import User

# Create your views here.
class UserViewSet(
    viewsets.GenericViewSet,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def create(self, request):
        """Register new user"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


class SearchUserListView(generics.ListAPIView):
    """Search and list users"""

    serializer_class = SearchUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.order_by("-nickname")
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "nickname"]


class LoginView(APIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        nickname = request.data["nickname"]
        password = request.data["password"]
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = authenticate(nickname=nickname, password=password)
            if not user:
                return Response(
                    {"error": "Credenciais Inválidas"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            response = Response(
                {
                    "id": user.id,
                    "name": user.name,
                    "nickname": user.nickname,
                    "access_token": user.token()["access"],
                    "refresh_token": user.token()["refresh"],
                },
                status=status.HTTP_200_OK,
            )

            accessExpirationTime = timezone.datetime.strftime(
                timezone.now() + timezone.timedelta(minutes=60),
                "%a, %d-%b-%Y %H:%M:%S GMT",
            )
            refreshExpirationTime = timezone.datetime.strftime(
                timezone.now() + timezone.timedelta(days=1),
                "%a, %d-%b-%Y %H:%M:%S GMT",
            )
            response.set_cookie(
                key="accesstoken",
                value=user.token()["access"],
                httponly=True,
                expires=accessExpirationTime,
            )
            response.set_cookie(
                key="refreshtoken",
                value=user.token()["refresh"],
                httponly=True,
                expires=refreshExpirationTime,
            )
            response.set_cookie(
                key="authtoken",
                value=uuid.uuid4(),
                expires=refreshExpirationTime,
            )

            return response


class ResetPasswordView(APIView):
    serializer_class = ResetPasswordSerializer
    permission_classes = [permissions.AllowAny]

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                user = User.objects.get(nickname=request.data["nickname"])
                serializer.update(instance=user, validated_data=request.data)
                return Response(
                    {"success": "Password redefinido com sucesso."},
                    status=status.HTTP_200_OK,
                )
            except:
                return Response({"error": ["Erro na busca de usuário"]})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
