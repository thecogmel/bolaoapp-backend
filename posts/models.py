from django.db import models

from accounts.models import User


class Post(models.Model):
    content = models.CharField(max_length=144, null=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
