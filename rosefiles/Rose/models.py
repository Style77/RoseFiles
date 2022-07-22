from datetime import datetime

from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ip_address_list = models.GenericIPAddressField

    permissions = models.IntegerField()  # 001

    def __str__(self):
          return "%s's profile" % self.user


def create_user_profile(sender, instance, created, **kwargs):
    if created:
       profile, created = UserProfile.objects.get_or_create(user=instance)


post_save.connect(create_user_profile, sender=User)


def upload_path_handler(instance, filename):
    return f"{instance.uploader.username}/{filename}"


class File(models.Model):
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)

    # file_name = models.CharField(max_length=128)
    #
    # # currently we're not limiting files to use of most popular extensions,
    # file_extension = models.CharField(max_length=8)

    description = models.CharField(max_length=128)

    views = models.BigIntegerField(default=0)  # all the page views
    downloads = models.BigIntegerField(default=0)  # all the downloads count
    # downloaders = models.JSONField()  # "{'username': 'downloads_count'}" -> "{'admin': 1}"
    upload_date = models.DateTimeField(default=datetime.now, blank=True)
    file = models.FileField(upload_to=upload_path_handler)
