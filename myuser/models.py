from django.contrib.auth.models import AbstractUser
from django.db import models



class MyUser(AbstractUser):
    position = models.CharField(max_length=120, blank=True, null=True)
    REQUIRED_FIELDS = ['position']

    def __str__(self):
        return self.username
