#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Categories.models import Category
from django.conf import settings

from django.db import models


class Stuff(models.Model):
    title = models.CharField(blank=True, max_length=120)
    description = models.TextField(blank=True)
    stored_timestamp = models.DateField(auto_created=True)

    # ForeignKeys
    category = models.ForeignKey(Category)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)


    class Meta:
        verbose_name = u'Вещь'
        verbose_name_plural = u'Вещи'

    def __unicode__(self):
        return self.title