# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey('auth.User') #User of django
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
                        default=timezone.now)
    published_date = models.DateTimeField(
                        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    ## In python 2 to show in select options for example use 'def __unicode__' and in python 3 use 'def __str__'
    def __unicode__(self):
        return u'%s' % self.title