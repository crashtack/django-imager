from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
import os
from io import open


HERE = os.path.dirname(os.path.abspath(__file__))
TEST_PHOTO_PATH = os.path.join(HERE, 'test_resorces', 'cover.png')


class AddPhotoTestCase(TestCase):

    def setUp(self):
        self.user = User(username='test_user')
        self.user.set_password('testpassword')
        self.user.save()
        self.url = reverse('upload_photo')

    def get_loged_in_response(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        return response

    def test_add_photo_view_requires_login(self):
        # import pdb; pdb.set_trace()
        login_url = reverse('auth_login')
        response = self.client.get(self.url, follow=True)
        self.assertEqual(response.status_code, 200)
        where_i_went = response.redirect_chain
        self.assertEqual(len(where_i_went), 1)
        self.assertEqual(where_i_went[0][1], 302)
        self.assertTrue(where_i_went[0][0].startswith(login_url))

    def test_add_photo_availibel_to_logged_in(self):
        response = self.get_loged_in_response()
        self.assertEqual(response.status_code, 200)

    def test_form_present_in_context(self):
        response = self.get_loged_in_response()
        self.assertIn('form', response.context)

    def test_uploading_photo_redirects_correctly(self):
        self.client.force_login(self.user)
        # import pdb; pdb.set_trace()
        with open(TEST_PHOTO_PATH, 'rb') as fh:
            data = {
                'title': 'second',
                'description': 'horay',
                'file': fh,
                'photographer': self.user.pk,
            }
            respones = self.client.post(self.url, data)
        self.assertEqual(respones.status_code, 302)


