from django.db import models
from django.conf import settings

from django.db.models.signals import post_save

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass