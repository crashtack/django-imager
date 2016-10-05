# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-05 02:44
from __future__ import unicode_literals

from django.db import migrations, models
import imager_images.models


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0004_auto_20161001_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='cover_photo',
            field=models.ImageField(blank=True, null=True, upload_to=imager_images.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='photo',
            name='height_field',
            field=models.IntegerField(blank=True, null=True, verbose_name='Height'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='width_field',
            field=models.IntegerField(blank=True, null=True, verbose_name='Width'),
        ),
    ]