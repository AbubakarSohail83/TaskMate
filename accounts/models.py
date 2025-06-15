from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
import hashlib

# this functions is used to save the avatar with a hashed prefix to avoid collisions
def user_avatar_path(instance, filename):
    hashed_prefix = hashlib.sha256(instance.username.encode('utf-8')).hexdigest()[:10]
    return f'avatars/user_{hashed_prefix}_{filename}'

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    country = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    area_of_interest = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to=user_avatar_path, blank=True)

