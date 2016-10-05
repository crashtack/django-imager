from __future__ import unicode_literals
from django.test import TestCase
from django.contrib.auth.models import User
from imager_profile.models import Photographer, PatronProfileManager
import datetime
from imagersite.tests.factories import UserFactory, AddressFactory
from imager_profile.models import Address


class ProfileTestCase(TestCase):

    def setUp(self):
        # self.user = UserFactory.build()
        self.user = UserFactory.create()
        self.client.force_login(user=self.user)
        # self.address = AddressFactory(photographer=self.user)
        self.today = datetime.date.today()

    def test_profile_is_created_when_user_is_saved(self):
        """tests the profile is created when a user is saved (Factoryboy)"""
        self.assertEqual(Photographer.objects.count(), 1)
        self.user = UserFactory.create()
        self.assertEqual(Photographer.objects.count(), 2)

    def test_profile_str_is_user_username(self):
        """tests Photographer __str__ returns user name"""
        self.user.save()
        profile = Photographer.objects.get(user=self.user)
        self.assertEqual(str(profile), self.user.username)

    def test_get_queryset(self):
        """tests that PatronProfileManager get_queryset returns only
            active users"""
        self.user.save()
        assert len(PatronProfileManager.get_queryset(self)) == 1
        self.user.is_active = False
        self.user.save()
        assert len(PatronProfileManager.get_queryset(self)) == 0
        # import pdb; pdb.set_trace()

    def test_is_active(self):
        """tests that the created user is activie"""
        self.user.save()
        # import pdb; pdb.set_trace()
        self.assertEquals(User.is_active, True)

    def test_address_title(self):
        """tests that the address has a title"""
        self.user.save()
        ad = Address(photographer=self.user)
        self.assertTrue(ad.title, 'Home')

    def test_address(self):
        """"test for a new address"""
        num_addess = 3
        self.user.addresses.add(*AddressFactory.create_batch(num_addess,
                                photographer=self.user))
        self.assertEquals(len(self.user.addresses.all()), num_addess)
        self.assertEquals(self.user.addresses.all()[0].title, 'Home')
        self.assertEquals(self.user.addresses.all()[0].state, 'WA')
        self.assertEquals(self.user.addresses.all()[0].post_code, '1234567')
