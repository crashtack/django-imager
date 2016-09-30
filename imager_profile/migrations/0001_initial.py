# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 22:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default', models.BooleanField(default=False, verbose_name='Default Address')),
                ('title', models.CharField(blank=True, default='Home', max_length=255, verbose_name='Title')),
                ('address_1', models.CharField(blank=True, default='', max_length=255, verbose_name='Street Address 1')),
                ('address_2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Street Address 2')),
                ('city', models.CharField(blank=True, default='', max_length=128, verbose_name='City')),
                ('state', models.CharField(blank=True, default='', max_length=2, verbose_name='State')),
                ('post_code', models.CharField(blank=True, default='', max_length=7, verbose_name='Zip Code')),
                ('photographer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='pirmary camera', max_length=255, verbose_name='Title')),
                ('eq_type', models.CharField(blank=True, max_length=200, null=True)),
                ('make', models.CharField(blank=True, max_length=200, null=True)),
                ('model', models.CharField(blank=True, max_length=200, null=True)),
                ('public', models.BooleanField(default=False)),
                ('photographer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='equipment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photographer',
            fields=[
                ('user_uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('bio', models.CharField(blank=True, max_length=1024, verbose_name='Bio')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Title')),
                ('public', models.BooleanField(default=False)),
                ('url', models.CharField(blank=True, max_length=255)),
                ('photographer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='socialmedia', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
