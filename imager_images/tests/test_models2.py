from __future__ import unicode_literals
from django.test import TestCase, override_settings
import datetime
import os
import tempfile
from imagersite.tests.factories import UserFactory, AlbumFactory, PhotoFactory


HERE = os.path.dirname(os.path.abspath(__file__))
TEST_PHOTO_PATH = os.path.join(HERE, "didrctoryt", "filename")
TEST_MEDIA = tempfile.mkdtemp()


class ModelTestCases(TestCase):

    def setUp(self):
        self.user = UserFactory.create()
        self.client.force_login(user=self.user)
        self.album = AlbumFactory(photographer=self.user)
        self.today = datetime.date.today()

    def test_album(self):
        # self.album = AlbumFactory(photographer=self.user)
        # self.client.force_login(user=self.user)
        self.assertTrue(self.album.published == 'private')
        self.assertTrue(type(self.album.title) == str)
        self.assertEqual(self.album.date_created, self.today)
        self.assertEqual(self.album.date_modified, self.today)
        self.assertEqual(self.album.date_pub, None)
        self.assertEqual(self.album.cover_photo, '')
        self.assertTrue(self.album.description is not None)

    @override_settings(MEDIA_ROOT=TEST_MEDIA)
    def test_album_many_photos(self):
        num_photos = 3
        self.album.photos.add(*PhotoFactory.create_batch(num_photos,
            photographer=self.user)
        )
        self.assertEquals(len(self.album.photos.all()), num_photos)
        self.assertEquals(self.album.photos.all()[0].published, 'private')
        self.assertEqual(self.album.photos.all()[0].date_created, self.today)
        self.assertEqual(self.album.photos.all()[0].date_modified, self.today)
        self.assertEqual(self.album.photos.all()[0].date_pub, None)

    @override_settings(MEDIA_ROOT=TEST_MEDIA)
    def test_photo(self):
        self.photo = PhotoFactory(photographer=self.user)
        self.assertTrue(self.photo.photographer.username == self.user.username)

