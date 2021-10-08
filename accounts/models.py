from django.db import models

# Create your models here.
class User(models.Model):

    email = models.EmailField(unique=True, max_length=60)
    password = models.CharField(max_length=120, blank=True, null=True)
    name = models.CharField(max_length=60)
    nickname = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return self.name
