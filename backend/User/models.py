from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    Password = models.CharField(max_length=100)
