# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 00:02
from __future__ import unicode_literals

from django.db import migrations, models
import imager_images.models


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='cover_photo',
            field=models.ImageField(upload_to=imager_images.models.user_directory_path),
        ),
    ]