# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-05 08:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_intro_test'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='intro_test',
            new_name='intro_text',
        ),
    ]
