from django.test import TestCase
from django.urls import reverse
from imagersite.tests.factories import UserFactory, AlbumFactory, PhotoFactory


class PhotoViewTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.create()
        self.client.force_login(user=self.user)
        self.photo = PhotoFactory(photographer=self.user)
        self.photo_response = self.client.get(reverse('photo', kwargs={'photo_id': self.photo.photo_id}))

    def test_photo_view_returns_ok_status(self):
        '''test that the response for photo is 200'''
        self.assertEquals(self.photo_response.status_code, 200)

    def test_photo_uses_correct_template(self):
        '''assert photo view is rendered with our templates'''
        for template_name in ['imagersite/base.html', 'imager_images/photo.html']:
            self.assertTemplateUsed(self.photo_response, template_name, count=1)

    def test_photo_view_displays_photo_name(self):
        '''test photo view displays photo name'''
        expected = self.photo.title
        self.assertContains(self.photo_response, expected)


# class AlbumViewTestCase(TestCase):

#     def setUp(self):
#         self.user = UserFactory.create()
#         self.client.force_login(user=self.user)
#         self.album = AlbumFactory(photographer=self.user)
#         self.album.cover_photo = PhotoFactory(photographer=self.user)
#         self.album_response = self.client.get(reverse('album', kwargs={'id': self.album.id}))

#     def test_album_view_returns_ok_status(self):
#         '''test that the response for album is 200'''
#         # import pbd; pdb.set_trace()
#         self.assertEquals(self.album_response.status_code, 200)
