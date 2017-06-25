from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.TextField(max_length=500, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    image_url = models.ImageField("avatar/", blank=True, null=True)

    def get_image_url(self, obj):
        request = self.context.get('request')
        photo_url = obj.image_url.url
        return request.build_absolute_uri(photo_url)
