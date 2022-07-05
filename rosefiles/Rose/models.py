from datetime import datetime

from django.db import models
from jsonfield import JSONField

from django.contrib.auth.models import User

# Create your models here.


def upload_path_handler(instance, filename):
    return f"files/{instance.uploader.username}/{filename}"


class File(models.Model):
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=128)

    # currently we're not limiting files to use of most popular extensions,
    # be careful because downloading suspicious files can lead to horrible things
    file_extension = models.CharField(max_length=8)

    views = models.BigIntegerField(default=0)  # all the page views
    downloads = models.BigIntegerField(default=0)  # all the downloads count
    downloaders = JSONField()  # "{'username': 'downloads_count'}" -> "{'admin': 1}"
    upload_date = models.DateTimeField(default=datetime.now, blank=True)
    file = models.FileField(upload_to=upload_path_handler)
