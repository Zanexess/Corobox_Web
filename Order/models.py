#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from Address.models import Address
from Categories.models import Category
import uuid, datetime
from django.utils import timezone


class CategoryOrder(models.Model):
    category = models.ForeignKey(Category)
    number = models.IntegerField()


class Order(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, default=0)
    created = models.DateTimeField(blank=True, default=datetime.datetime.now())
    address = models.ForeignKey(Address, default=0)
    status = models.CharField(max_length=120, default="PROCESS")
    order = models.ManyToManyField(CategoryOrder)

    class Meta:
        verbose_name = u'Заказ'
        verbose_name_plural = u'Заказы'

    def __unicode__(self):
        return str(self.owner)
