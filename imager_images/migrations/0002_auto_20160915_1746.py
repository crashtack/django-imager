# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-15 17:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='image_file',
            new_name='file',
        ),
    ]
