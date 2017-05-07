#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Address(models.Model):
    street = models.CharField(max_length=255)
    house = models.CharField(max_length=120)
    access = models.CharField(max_length=120)
    floor = models.CharField(max_length=120)
    flat = models.CharField(max_length=120)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        verbose_name = u'Адрес'
        verbose_name_plural = u'Адреса'

    def __unicode__(self):
        return self.street