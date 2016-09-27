from __future__ import unicode_literals
from django.test import TestCase
from django.contrib.auth.models import User
import factory
from imager_profile.models import Photographer, PatronProfileManager
from imager_profile.models import Address
from django.core import mail
from registration.backends.hmac.views import RegistrationView


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
        '''tests the profile is created when a user is saved (Factoryboy)'''

        self.assertTrue(Photographer.objects.count() == 0)
        self.user.save()
        self.assertTrue(Photographer.objects.count() == 1)

    def test_profile_str_is_user_username(self):
        '''tests Photographer __str__ returns user name'''
        self.user.save()
        profile = Photographer.objects.get(user=self.user)
        self.assertEqual(str(profile), self.user.username)

    def test_get_queryset(self):
        '''tests that PatronProfileManager get_queryset returns only
            active users'''
        self.user.save()
        assert len(PatronProfileManager.get_queryset(self)) == 1
        self.user.is_active = False
        self.user.save()
        assert len(PatronProfileManager.get_queryset(self)) == 0
        # import pdb; pdb.set_trace()

    def test_is_active(self):
        '''tests that the created user is activie'''
        self.user.save()
        # import pdb; pdb.set_trace()
        self.assertEquals(User.is_active, True)

    def test_address_title(self):
        self.user.save()
        # import pdb; pdb.set_trace()
        ad = Address(photographer=self.user.photographer)
        self.assertTrue(ad.title, 'Home')


    # def test_email_on_registration(self):
    #     creat_inactive_user(self, form)
    #     self.assertEqual(len(mail.outbox), 1)


# class EmailTest(TestCase):
#     def test_send_email(self):
#         # Send message.
#         mail.send_mail(
#             'Subject here', 'Here is the message.',
#             'from@example.com', ['to@example.com'],
#             fail_silently=False,
#         )

#         # Test that one message has been sent.
#         self.assertEqual(len(mail.outbox), 1)

#         # Verify that the subject of the first message is correct.
#         self.assertEqual(mail.outbox[0].subject, 'Subject here')
