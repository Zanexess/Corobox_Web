#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    max_weight = models.FloatField()
    monthly_price = models.IntegerField(default=0)

    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'

    def __unicode__(self):
        return self.title