from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(
        self,
        email,
        name,
        nickname,
        password=None,
    ):

        user = self.model(
            email=self.normalize_email(email).lower(),
            name=name,
            nickname=nickname,
        )
        if password != None:
            user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, name, nickname):

        user = self.create_user(
            email=email, name=name, password=password, nickname=nickname
        )

        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser):

    email = models.EmailField(unique=True, max_length=60)
    password = models.CharField(max_length=120, blank=True, null=True)
    name = models.CharField(max_length=60)
    nickname = models.CharField(max_length=60, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = (
        "name",
        "nickname",
    )

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def __str__(self):
        return self.email
