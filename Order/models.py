#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from Address.models import Address
from Stuff.models import Stuff
from Categories.models import Category
import uuid, datetime
from django.utils import timezone


class CategoryOrder(models.Model):
    category = models.ForeignKey(Category)
    number = models.IntegerField()

    class Meta:
        verbose_name = u'Категория и количество'
        verbose_name_plural = u'Категория и количество'

class Order(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, default=0)
    created = models.DateTimeField(blank=True, default=datetime.datetime.now())
    till = models.DateTimeField(blank=True, default=datetime.datetime.now())
    address = models.ForeignKey(Address, default=0)
    status = models.CharField(max_length=120, default="PROCESS")
    order = models.ManyToManyField(CategoryOrder)

    class Meta:
        verbose_name = u'Заказ на склад'
        verbose_name_plural = u'Заказы на склад'

    def __unicode__(self):
        return str(self.owner)


class OrderFrom(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, default=0)
    created = models.DateTimeField(blank=True, default=datetime.datetime.now())
    address = models.ForeignKey(Address, default=0)
    status = models.CharField(max_length=120, default="PROCESS")
    stuff = models.ManyToManyField(Stuff)

    class Meta:
        verbose_name = u'Заказ со склада'
        verbose_name_plural = u'Заказы со склада'

    def __unicode__(self):
        return str(self.owner)
