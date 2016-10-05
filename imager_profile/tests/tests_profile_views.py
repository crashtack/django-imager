from django.test import TestCase
from django.urls import reverse


class ProfileViewTestCase(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('private_profile'))
