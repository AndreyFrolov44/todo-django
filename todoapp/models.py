from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from django.utils import timezone
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = CustomUserManager()

    def get_short_name(self):
        return self.username

    def natural_key(self):
        return self.username

    def __str__(self):
        return self.username


class TodoBlock(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    date_add = models.DateTimeField(default=timezone.now)
    date_close = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class TodoItem(models.Model):
    name = models.CharField(max_length=250)
    block = models.ForeignKey(TodoBlock, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    date_add = models.DateTimeField(default=timezone.now)
    date_close = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name





