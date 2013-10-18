# -*- encoding: utf-8 -*-
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=255, verbose_name=u'Imię/nick')

class Activity(models.Model):
    person = models.ForeignKey(Person)
    timestamp = models.DateTimeField(auto_now_add=True)
    item = models.CharField(max_length=255, verbose_name=u'Zakup')