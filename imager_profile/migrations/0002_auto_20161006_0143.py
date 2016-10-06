# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-06 01:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imager_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photographer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='photographer', to=settings.AUTH_USER_MODEL),
        ),
    ]
