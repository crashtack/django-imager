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
        qs = super(PatronProfileManager, self).get_queryset()
        return qs.filter(user__is_active=True)


@python_2_unicode_compatible
class Photographer(models.Model):
    user_uuid = models.UUIDField(primary_key=True,
                                 default=uuid.uuid4,
                                 editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    has_portfolios = models.BooleanField(default=False)
    portfolio_url = models.CharField(max_length=255, blank=True)

    def __str__(self):
        fn = self.user.get_full_name().strip() or self.user.get_username()
        return "{}: {}".format(fn, self.user_uuid)

    @property
    def is_active(self):
        return self.user.is_active

    objects = models.Manager()
    active = PatronProfileManager()


class Address(models.Model):
    photographer_profile = models.ForeignKey(
        Photographer,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='Addresses',  # TODO: look this up and set it
    )
    default = models.BooleanField('Default Address', default=False)
    address_1 = models.CharField('Street Address 1',
                                 max_length=255,
                                 blank=True,  # it's valid to be empty in Python
                                 null=True)   # allow it to be empty in DB
    address_2 = models.CharField('Street Address 2',
                                 max_length=255,
                                 blank=True,
                                 null=True)
    city = models.CharField('City',
                            max_length=128,
                            blank=True,
                            null=True)
    state = models.CharField('State',
                             max_length=2,
                             blank=True,
                             null=True)
    post_code = models.CharField('Zip Code',
                                 max_length=7,
                                 blank=True,
                                 null=True)


class Equipment(models.Model):
    equipment_type = models.CharField(max_length=200, blank=True, null=True)
    make = models.CharField(max_length=200, blank=True, null=True)
    model = models.CharField(max_length=200, blank=True, null=True)


class SocialMedia(models.Model):
    photographer_profile = models.ForeignKey(
        Photographer,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='SocialMedia',  # TODO: look this up and set it
    )
    reason_i_like_bacon = models.CharField(max_length=200,
                                           blank=True,
                                           null=True)
    # more fields
