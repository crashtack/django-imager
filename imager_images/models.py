from __future__ import unicode_literals
import uuid
from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible


def user_directory_path(instance, filename):
    ''' file will be uploaded to MEDIA_ROOT/user_<id>/%Y%m%d<filename>
        this is not true it will return: MEDIA_ROOT/user_<id>/<filename>
    '''
    return 'user_{0}/%Y%m%d/{1}'.format(instance.user.id, filename)


class Photo(models.Model):
    '''A Photo belonging to a usr'''
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    albums = models.ManyToManyField('Album')
    photo_id = models.UUIDField(primary_key=True,
                                default=uuid.uuid4,
                                editable=False)

    file = models.ImageField(upload_to=user_directory_path,
                             height_field=None,
                             width_field=None, max_length=100)

    title = models.CharField("Title", max_length=255, blank=True)
    height_field = models.IntegerField("Height", blank=True)
    width_field = models.IntegerField("Width", blank=True)
    latitude = models.IntegerField("Latitude", blank=True)
    longitude = models.IntegerField("Longitude", blank=True)
    camera = models.CharField("Camera", max_length=64, blank=True)
    lens = models.CharField("Lens", max_length=64, blank=True)
    focal_length = models.CharField("Focal Length", max_length=32, blank=True)
    shutter_speed = models.IntegerField("Shutter Speed", blank=True)
    appature = models.CharField("Title", max_length=64, blank=True)
    description = models.CharField("Title", max_length=255, blank=True)
    date_created = models.DateField('Date Created', auto_now_add=True)
    date_modified = models.DateField('Date Modified', auto_now=True)
    date_pub = models.DateField('Date Published', editable=True, blank=True)
    published = models.CharField(max_length=64,
                                 choices=[('private', 'private'),
                                          ('shared', 'shared'),
                                          ('public', 'public')])
    likes_cheese = models.BooleanField('Likes Cheese!', default=False)

    def __str__(self):
        '''this is a  doc string'''
        return self.image_file

    class Meta:
        ordering = ('date_created',)


class Album(models.Model):
    '''An Album of Photos'''
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    title = models.CharField("Title", max_length=255, blank=True)
    description = models.CharField("Description", max_length=255, blank=True)
    cover_photo = models.CharField("Cover Photo", max_length=255, blank=True)
    date_created = models.DateField('Date Created', auto_now_add=True)
    date_modified = models.DateField('Date Modified', auto_now=True)
    date_pub = models.DateField('Date Published', editable=True, blank=True)
    published = models.CharField(max_length=64,
                                 choices=[('private', 'private'),
                                          ('shared', 'shared'),
                                          ('public', 'public')])

    def __str__(self):
        return self.title
