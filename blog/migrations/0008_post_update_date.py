# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-14 18:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20161008_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='update_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]