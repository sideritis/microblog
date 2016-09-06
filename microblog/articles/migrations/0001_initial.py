# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-05 19:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Title')),
                ('slug', models.SlugField(max_length=80, verbose_name='Slug')),
                ('text', models.TextField(verbose_name='Text')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='Image')),
                ('publish', models.BooleanField(default=False, verbose_name='Publish')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('tags', models.ManyToManyField(to='tags.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
    ]