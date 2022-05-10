from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(
        self,
        name,
        nickname,
        password=None,
    ):

        user = self.model(
            name=name,
            nickname=nickname,
        )
        if password != None:
            user.set_password(password)
        user.save()
        return user

    def create_superuser(self, password, name, nickname):

        user = self.create_user(name=name, password=password, nickname=nickname)

        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser):

    name = models.CharField(max_length=60)
    password = models.CharField(max_length=120, blank=True, null=True)
    nickname = models.CharField(unique=True, max_length=60, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "nickname"
    REQUIRED_FIELDS = ("name",)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def token(self):
        refreshToken = RefreshToken.for_user(self)
        return {"refresh": str(refreshToken), "access": str(refreshToken.access_token)}

    def __str__(self):
        return self.nickname
