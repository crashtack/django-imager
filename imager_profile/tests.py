from __future__ import unicode_literals
from django.test import TestCase
from django.contrib.auth.models import User
import factory
from imager_profile.models import Photographer


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = 'bob'
    email = factory.LazyAttribute(
        lambda x: "{}@example.com".format(x.username)
    )


class ProfileTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.create()
        self.user.set_password('secret')
        self.user.save()

    def test_foo(self):
        import pdb; pdb.set_trace()
        self.assertTrue(True)
