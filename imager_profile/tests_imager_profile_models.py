from __future__ import unicode_literals
from django.test import TestCase
from django.contrib.auth.models import User
import factory
from faker import Factory as FakerFactory
from factory import post_generation, lazy_attribute
from imager_profile.models import Photographer, PatronProfileManager
from imager_profile.models import Address, Equipment, SocialMedia
from django.core import mail
from registration.backends.hmac.views import RegistrationView
import datetime

fake = FakerFactory.create()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "user{}".format(n))
    email = factory.Sequence(
        lambda n: "user{}@example.com".format(n)
    )


class AddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Address

    photographer = factory.SubFactory(UserFactory)
    address_1 = factory.lazy_attribute(lambda o: fake.sentence(nb_words=2))
    city = factory.lazy_attribute(lambda o: fake.sentence(nb_words=1))
    state = 'WA'
    post_code = 1234567


class EquipmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Equipment

    photographer = factory.SubFactory(UserFactory)
    model = factory.lazy_attribute(lambda o: fake.sentence(nb_words=2))


class SocialFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SocialMedia

    photographer = factory.SubFactory(UserFactory)
    url = 'http://fakebook.com/user1234'


class ProfileTestCase(TestCase):

    def setUp(self):
        # self.user = UserFactory.build()
        self.user = UserFactory.create()
        self.client.force_login(user=self.user)
        # self.address = AddressFactory(photographer=self.user)
        self.today = datetime.date.today()

    def test_profile_is_created_when_user_is_saved(self):
        '''tests the profile is created when a user is saved (Factoryboy)'''
        self.assertEqual(Photographer.objects.count(), 1)
        self.user = UserFactory.create()
        self.assertEqual(Photographer.objects.count(), 2)

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
        ad = Address(photographer=self.user)
        self.assertTrue(ad.title, 'Home')

    def test_address(self):
        "test for a new address"
        num_addess = 3
        self.user.addresses.add(*AddressFactory.create_batch(num_addess,
            photographer=self.user))
        self.assertEquals(len(self.user.addresses.all()), num_addess)
        self.assertEquals(self.user.addresses.all()[0].title, 'Home')
        self.assertEquals(self.user.addresses.all()[0].state, 'WA')
        self.assertEquals(self.user.addresses.all()[0].post_code, '1234567')

    def test_equipment(self):
        "test for a new address"
        num_equip = 3
        self.user.equipment.add(*EquipmentFactory.create_batch(num_equip,
            photographer=self.user))
        self.assertEquals(len(self.user.equipment.all()), num_equip)
        self.assertEquals(self.user.equipment.all()[0].title, 'pirmary camera')
        self.assertEquals(self.user.equipment.all()[0].public, False)
        self.assertNotEquals(self.user.equipment.all()[0].model, '')

    def test_social_media(self):
        "test for a new address"
        num_soc = 3
        self.user.socialmedia.add(*SocialFactory.create_batch(num_soc, photographer=self.user))
        self.assertEquals(len(self.user.socialmedia.all()), num_soc)
        self.assertEquals(self.user.socialmedia.all()[0].title, '')
        self.assertEquals(self.user.socialmedia.all()[0].public, False)
        self.assertEquals(self.user.socialmedia.all()[0].url,
            'http://fakebook.com/user1234')

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
