# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-21 17:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0004_auto_20160921_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='slug',
        ),
    ]
