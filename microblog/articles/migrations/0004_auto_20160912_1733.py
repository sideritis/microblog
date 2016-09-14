# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-12 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20160906_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(max_length=80, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=80, unique=True, verbose_name='Title'),
        ),
    ]