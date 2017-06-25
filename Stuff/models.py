#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Categories.models import Category
from django.conf import settings
from django.db import models
import datetime, uuid


class Stuff(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(blank=True, max_length=120)
    description = models.TextField(blank=True)
    stored_timestamp = models.DateTimeField(blank=True, default=datetime.datetime.now())
    till = models.DateTimeField(blank=True, default=datetime.datetime.now())
    image_url = models.ImageField(upload_to='stuff/', blank=True)
    status = models.CharField(default="stored", blank=False, max_length=50)

    # ForeignKeys
    category = models.ForeignKey(Category)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        verbose_name = u'Вещь'
        verbose_name_plural = u'Вещи'

    def __unicode__(self):
        return self.title
