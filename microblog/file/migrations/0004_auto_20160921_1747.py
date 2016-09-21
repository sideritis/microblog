# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-21 17:47
from __future__ import unicode_literals

from django.db import migrations, models
import file.models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0003_auto_20160921_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='file/', validators=[file.models.validate_file_extension], verbose_name='Upload file'),
        ),
    ]
