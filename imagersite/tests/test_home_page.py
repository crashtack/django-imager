from django.test import TestCase
from django.urls import reverse


class HomePageTestCase(TestCase):

    """ The first test to run:
        Is there a view?
    def exists(self):
        response = self.response.client.get('/')
        self.assertEquals(response.status_code, 200)
    """

    def setUp(self):
        # self.response = self.client.get('/')
        self.response = self.client.get(reverse('homepage'))

    def tearDown(self):
        pass

    def test_home_page_exists(self):
        '''assert that the rewpose for the hoepageurl is 200'''
        self.assertEquals(self.response.status_code, 200)

    def test_for_registration_botton(self):
        '''assert that theresponse contains a iling to the resirataion page'''
        # import pdb; pdb.set_trace()
        reg_url = reverse('registration_register')
        expected = 'href="{}"'.format(reg_url)
        self.assertContains(self.response, expected, status_code=200)

    def test_uses_correct_template(self):
        '''assert the home page view is rendered with our templates'''
        for template_name in ["imagersite/base.html", 'imagersite/home.html']:
            self.assertTemplateUsed(self.response, template_name, count=1)

    def test_login_botton(self):
        '''assert homepage has login button'''
        login_url = reverse('login')
        expected = 'href="{}"'.format(login_url)
        self.assertContains(self.response, expected, status_code=200)

    def test_context_contains_photo_file_path(self):
        """assert the context contains the image file path"""
        self.assertTrue("photo" in self.response.context)
        # self.response.context["foo"]
