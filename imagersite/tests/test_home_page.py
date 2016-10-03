from django.test import TestCase
from django.urls import reverse


class HomePageTestCase(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('homepage'))

    def test_home_page_exists(self):
        '''assert that the rewpose for the hoepageurl is 200'''
        self.assertEquals(self.response.status_code, 200)

    def test_for_registration_button(self):
        '''assert that theresponse contains a link to the resirataion page'''
        reg_url = reverse('registration_register')
        expected = 'href="{}"'.format(reg_url)
        self.assertContains(self.response, expected, status_code=200)

    def test_uses_correct_template(self):
        '''assert the home page view is rendered with our templates'''
        for template_name in ["imagersite/base.html", 'imagersite/home.html']:
            self.assertTemplateUsed(self.response, template_name, count=1)

    # def test_login_botton(self):
    #     '''assert homepage has login button'''
    #     login_url = reverse('login')
    #     expected = 'href="{}"'.format(login_url)
    #     self.assertContains(self.response, expected, status_code=200)

    def test_context_contains_photo(self):
        """assert the context contains a photo file path"""
        self.assertTrue("photo" in self.response.context)
