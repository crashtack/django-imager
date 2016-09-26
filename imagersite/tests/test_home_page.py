from django.test import TestCase


class HomePageTestCase(TestCase):

    def setUp(self):
        self.response = self.client.get('/')

    def tearDown(self):
        pass

    def test_home_page_exists(self):
        '''assert that the rewpose for the hoepageurl is 200'''
        self.assertEquals(self.response.status_code, 200)

    def test_for_registration_botton(self):
        '''assert that theresponse contains a iling to the resirataion page'''
        # import pdb; pdb.set_trace()
        expected = '/accounts/register/'
        self.assertContains(self.response, expected)
