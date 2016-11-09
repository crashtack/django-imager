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
        """test add photo view requires login"""
        # import pdb; pdb.set_trace()
        login_url = reverse('auth_login')
        response = self.client.get(self.url, follow=True)
        self.assertEqual(response.status_code, 200)
        where_i_went = response.redirect_chain
        self.assertEqual(len(where_i_went), 1)
        self.assertEqual(where_i_went[0][1], 302)
        self.assertTrue(where_i_went[0][0].startswith(login_url))

    def test_add_photo_availibel_to_logged_in(self):
        """test add photo view is availibel to logged in"""
        response = self.get_loged_in_response()
        self.assertEqual(response.status_code, 200)

    def test_form_present_in_context(self):
        """test there is a form on the add photoview"""
        response = self.get_loged_in_response()
        self.assertIn('form', response.context)

    def test_uploading_photo_redirects(self):
        """test_uploading_photo_redirects_correctly"""
        self.client.force_login(self.user)
        with open(TEST_PHOTO_PATH, 'rb') as fh:
            data = {
                'title': 'second',
                'description': 'horay',
                'file': fh,
                'photographer': self.user.pk,
                'published': 'private'
            }
            respones = self.client.post(self.url, data)
        self.assertEqual(respones.status_code, 302)


class AddAlbumTestCase(TestCase):

    def setUp(self):
        self.user = User(username='test_user')
        self.user.set_password('testpassword')
        self.user.save()
        self.url = reverse('add_album')

    def get_loged_in_response(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        return response

    def test_add_album_view_requires_login(self):
        """test add album view requires login"""
        login_url = reverse('auth_login')
        response = self.client.get(self.url, follow=True)
        self.assertEqual(response.status_code, 200)
        where_i_went = response.redirect_chain
        self.assertEqual(len(where_i_went), 1)
        self.assertEqual(where_i_went[0][1], 302)
        self.assertTrue(where_i_went[0][0].startswith(login_url))

    def test_add_album_availibel_to_logged_in(self):
        """test add album view is availibel to logged in"""
        response = self.get_loged_in_response()
        self.assertEqual(response.status_code, 200)

    def test_form_present_in_context(self):
        """test there is a form on the add album view"""
        response = self.get_loged_in_response()
        self.assertIn('form', response.context)

    def test_uploading_album_redirects(self):
        """test_uploading_photo_redirects_correctly"""
        self.client.force_login(self.user)
        data = {
            'title': 'second',
            'description': 'horay',
            'published': 'private',
            'photographer': self.user.pk,
        }
        respones = self.client.post(self.url, data)
        self.assertEqual(respones.status_code, 302)
