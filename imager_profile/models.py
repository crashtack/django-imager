from __future__ import unicode_literals
from django.db import models
import uuid
from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.db.models.signals import post_save
from django.dispatch import receiver

import logging
logr = logging.getLogger(__name__)


@receiver(post_save, sender=User)
def make_sure_user_profile_is_added_on_user_created(sender, **kwargs):
    if kwargs.get('created', False):
        up = User_Profile.objects.create(user=kwargs.get('instance'))
        loger.debut('User_Profile created {}'.format(up))


@python_2_unicode_compatible
class Photographer(models.Model):
    user_uuid = models.UUIDField(primary_key=True,
                                   default=uuid.uuid4,
                                   editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    has_portfolio = models.BooleanField()

    def __str__(self):
        fn = self.user.get_full_name().strip() or self.user.get_username()
        return "{}: {}".format(fn, self.user_number)

    def active():
        pass


class Address(models.Model):
    address_1 = models.CharField('Street Address 1',
                                 max_length=255,
                                 blank=True,
                                 null=True)
    address_2 = models.CharField('Street Address 2',
                                 max_length=255,
                                 blank=True,
                                 null=True)
    city = models.CharField(max_length=128,
                                 blank=True,
                                 null=True)
    state = models.CharField(max_length=2,
                                 blank=True,
                                 null=True)
    post_code = models.CharField(max_length=7,
                                 blank=True,
                                 null=True)


class Equipment(models.Model):
    equipment_type = models.CharField(max_length=200, blank=True, null=True)
    make = models.CharField(max_length=200, blank=True, null=True)
    model = models.CharField(max_length=200, blank=True, null=True)
