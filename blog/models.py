# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class PostType(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(default="", max_length=50)
    description = models.CharField(default="", max_length=200, blank=True)
    created_date = models.DateField(default=timezone.now)

    def publish(self):
        self.save()

    ## In python 2 to show in select options for example use 'def __unicode__' and in python 3 use 'def __str__'
    def __unicode__(self):
        return u'%s - %s' % (self.type, self.description)

    class Meta:
        unique_together = (("type",),)

class PostCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=50)
    description = models.CharField(default="", max_length=200, blank=True)
    created_date = models.DateTimeField(default = timezone.now)

    def publish(self):
        self.save()

    ## In python 2 to show in select options for example use 'def __unicode__' and in python 3 use 'def __str__'
    def __unicode__(self):
        return u'%s - %s' % (self.name, self.description)

    class Meta:
        unique_together = (("name",),)


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey('auth.User')  # User of django
    title = models.CharField(max_length=200)
    text = models.TextField()
    type = models.ForeignKey(PostType)
    category = models.ForeignKey(PostCategory)
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
