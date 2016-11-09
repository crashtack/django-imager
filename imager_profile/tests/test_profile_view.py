from django.test import TestCase
from django.urls import reverse
from imagersite.tests.factories import ValidatedUserFactory


class ProfileViewNotLoggedInTestCase(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('private_profile'))

    def test_private_profile_redirects_not_logged_in(self):
        '''assert that the response for the private profile is 200'''
        self.assertEquals(self.response.status_code, 302)


class ProfileViewLoggedInTestCase(TestCase):

    def setUp(self):
        self.user = ValidatedUserFactory.create()
        self.client.force_login(user=self.user)
        self.response = self.client.get(reverse('private_profile'))

    def test_private_profile_status_logged_in(self): 
        '''assert that the response for the private profile is 200'''
        self.assertEquals(self.response.status_code, 200)

    def test_uses_correct_template(self):
        '''assert the home page view is rendered with our templates'''
        for template_name in ['imagersite/base.html', 'imager_profile/private_profile.html']:
            self.assertTemplateUsed(self.response, template_name, count=1)

    def test_private_profile_has_link_to_library(self):
        ''' test private profile has link to library'''
        expected = b'href="/images/library/"'
        self.assertTrue(expected in self.response.content)

    def test_private_profile_displays_users_username(self):
        ''' test private profile has link to library'''
        expected = self.user.username
        self.assertContains(self.response, expected)

