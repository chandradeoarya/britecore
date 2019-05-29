from django.db import models
from django.conf import settings

from django.db.models.signals import post_save

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)


def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        default_user = User.objects.get(id=1)
        default_user.followers.add(instance)


post_save.connect(post_save_user_receiver, sender=User)
