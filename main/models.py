# -*- encoding: utf-8 -*-
from datetime import date
from django.utils.timesince import timesince, timeuntil
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=255, verbose_name=u'Imię/nick')

    def __unicode__(self):
        return self.name

class Activity(models.Model):
    person = models.ForeignKey(Person)
    timestamp = models.DateTimeField(auto_now_add=True)
    item = models.CharField(max_length=255, verbose_name=u'Zakup')

    timestamp.editable=True

    def is_today(self):
        return self.timestamp.date() == date.today()

    def human_timestamp(self):
        str = timesince(self.timestamp)
        if u',' in str:
            str = str.split(',')[0]
        return str

    @classmethod
    def get_latest_activity(cls):
        activity = Activity.objects.order_by('-timestamp')[:1]
        if len(activity) == 0:
            return None
        return activity[0]

    @classmethod
    def today_was_done(cls):
        activity = Activity.get_latest_activity()
        if activity is None:
            return False
        return activity.is_today()

    def __unicode__(self):
        return unicode(self.person) + u' poszedł po ' + self.item