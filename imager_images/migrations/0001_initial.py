# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-17 17:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imager_images.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Title')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Description')),
                ('cover_photo', models.ImageField(blank=True, null=True, upload_to=imager_images.models.user_directory_path)),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='Date Created')),
                ('date_modified', models.DateField(auto_now=True, verbose_name='Date Modified')),
                ('published', models.CharField(choices=[('private', 'private'), ('shared', 'shared'), ('public', 'public')], default='private', max_length=64)),
                ('photographer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='albums', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('photo_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('file', models.ImageField(upload_to=imager_images.models.user_directory_path)),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Title')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Description')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='Date Created')),
                ('date_modified', models.DateField(auto_now=True, verbose_name='Date Modified')),
                ('date_pub', models.DateField(blank=True, null=True, verbose_name='Date Published')),
                ('published', models.CharField(choices=[('private', 'private'), ('shared', 'shared'), ('public', 'public')], default='private', max_length=64)),
                ('albums', models.ManyToManyField(blank=True, related_name='photos', to='imager_images.Album')),
                ('photographer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', related_query_name='photo', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('date_created',),
            },
        ),
    ]
