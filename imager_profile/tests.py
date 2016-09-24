from __future__ import unicode_literals
from django.test import TestCase
from django.contrib.auth.models import User
import factory
from imager_profile.models import Photographer


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "user{}".format(n))
    email = factory.Sequence(
        lambda n: "user{}@example.com".format(n)
    )


class ProfileTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.build()

    def test_profile_is_created_when_user_is_saved(self):
        self.assertTrue(Photographer.objects.count() == 0)
        self.user.save()
        self.assertTrue(Photographer.objects.count() == 1)

    def test_profile_str_is_user_username(self):
        self.user.save()
        profile = Photographer.objects.get(user=self.user)
        self.assertEqual(str(profile), self.user.username)
