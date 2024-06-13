import os
from django.db.models.signals import post_delete
from django.dispatch import receiver

from apps.users.models import CustomUser


@receiver(post_delete, sender=CustomUser)
def delete_photo_on_delete_user(instance, *args, **kwargs):
    if instance.image:
        os.remove(instance.image.path)
