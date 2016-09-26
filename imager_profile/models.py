from __future__ import unicode_literals
from django.db import models
import uuid
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.db.models.signals import post_save
from django.dispatch import receiver

import logging
logr = logging.getLogger(__name__)


@receiver(post_save, sender=User)
def make_sure_user_profile_is_added_on_user_created(sender, **kwargs):
    if kwargs.get('created', False):
        up = Photographer.objects.create(user=kwargs.get('instance'))
        # loger.debut('User_Profile created {}'.format(up))


class PatronProfileManager(models.Manager):
    '''returns a queryset pre-filters to only active profiles'''
    class Meta:
        model = "PatronProfile"

    def get_queryset(self):
        '''retrn a queryset of active users'''
        return User.objects.filter(is_active=True)


@python_2_unicode_compatible
class Photographer(models.Model):
    user_uuid = models.UUIDField(primary_key=True,
                                 default=uuid.uuid4,
                                 editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                )

    def __str__(self):
        return self.user.get_full_name() or self.user.username

    @property
    def is_active(self):
        return self.user.is_active

    objects = models.Manager()
    active = PatronProfileManager()


class Address(models.Model):
    photographer = models.ForeignKey(Photographer,
                                     on_delete=models.CASCADE,
                                     blank=True,)
    default = models.BooleanField('Default Address', default=False)
    title = models.CharField('Title',
                             max_length=255,
                             blank=True,
                             default='Home')
    address_1 = models.CharField('Street Address 1',
                                 max_length=255,
                                 blank=True,
                                 default='')   # allow it to be empty in DB
    address_2 = models.CharField('Street Address 2',
                                 max_length=255,
                                 blank=True,
                                 null=True)
    city = models.CharField('City',
                            max_length=128,
                            blank=True,
                            default='')
    state = models.CharField('State',
                             max_length=2,
                             blank=True,
                             default='')
    post_code = models.CharField('Zip Code',
                                 max_length=7,
                                 blank=True,
                                 default='')

    def __str__(self):
        '''this is a  doc string'''
        return '{}: {}'.format(self.photographer.user, self.title)


class Equipment(models.Model):
    photographer = models.ForeignKey(Photographer,
                                     on_delete=models.CASCADE,
                                     blank=True,)
    title = models.CharField('Title',
                             max_length=255,
                             blank=True,
                             default='Home')
    eq_type = models.CharField(max_length=200, blank=True, null=True)
    make = models.CharField(max_length=200, blank=True, null=True)
    model = models.CharField(max_length=200, blank=True, null=True)
    public = models.BooleanField(default=False)


class SocialMedia(models.Model):
    photographer = models.ForeignKey(Photographer,
                                     on_delete=models.CASCADE,
                                     blank=True,)
    title = models.CharField('Title',
                             max_length=255,
                             blank=True,)
    public = models.BooleanField(default=False)
    url = models.CharField(max_length=255, blank=True)
