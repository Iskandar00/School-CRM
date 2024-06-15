import os
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

from apps.general.services import delete_file_after_delete_obj, normalize_text
from apps.users.models import CustomUser


@receiver(post_delete, sender=CustomUser)
def delete_photo_on_delete_user(instance, *args, **kwargs):
    delete_file_after_delete_obj(instance)
