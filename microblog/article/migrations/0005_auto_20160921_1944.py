# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-21 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20160921_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='desc',
            field=models.CharField(default='', max_length=400, verbose_name='Description'),
        ),
    ]
