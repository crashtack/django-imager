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


class AlbumViewTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.create()
        self.client.force_login(user=self.user)
        self.album = AlbumFactory(photographer=self.user)
        self.album.cover_photo = PhotoFactory(photographer=self.user)
        self.album_response = self.client.get(reverse('album', kwargs={'pk': self.album.id}))

    def test_album_view_returns_ok_status(self):
        '''test that the response for album is 200'''
        self.assertEquals(self.album_response.status_code, 200)

    def test_album_uses_correct_template(self):
        '''assert album view is rendered with our templates'''
        for template_name in ['imagersite/base.html', 'imager_images/album.html']:
            self.assertTemplateUsed(self.album_response, template_name, count=1)

    def test_album_view_displays_album_name(self):
        '''test album view displays album name'''
        expected = self.album.title
        self.assertContains(self.album_response, expected)


class LibraryViewTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.create()
        self.client.force_login(user=self.user)
        self.album = AlbumFactory(photographer=self.user)
        self.album.cover_photo = PhotoFactory(photographer=self.user)
        self.photo = PhotoFactory(photographer=self.user)
        self.library_response = self.client.get(reverse('personal_library'))

    def test_library_view_returns_ok_status(self):
        '''test that the response for album is 200'''
        self.assertEquals(self.library_response.status_code, 200)

    def test_library_uses_correct_template(self):
        '''assert album view is rendered with our templates'''
        for template_name in ['imagersite/base.html', 'imager_images/library.html']:
            self.assertTemplateUsed(self.library_response, template_name, count=1)

    def test_library_view_displays_photo_and_album_name(self):
        '''test album view displays album name'''
        # import pdb; pdb.set_trace()
        expected_album = self.album.title
        expected_photo = self.photo.title
        self.assertContains(self.library_response, expected_album)
        self.assertContains(self.library_response, expected_photo)
