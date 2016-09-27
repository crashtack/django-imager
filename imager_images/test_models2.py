from __future__ import unicode_literals
from django.test import TestCase
import factory
# from faker import Faker
from faker import Factory as FakerFactory
from factory import post_generation, lazy_attribute
from django.contrib.auth.models import User
from imager_images.models import Photo, Album
import datetime


fake = FakerFactory.create()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "user{}".format(n))
    email = factory.Sequence(
        lambda n: "user{}@example.com".format(n)
    )


class AlbumFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Album

    photographer = factory.SubFactory(UserFactory)

    title = factory.lazy_attribute(lambda o: fake.sentence(nb_words=4))
    description = factory.lazy_attribute(lambda o: fake.sentence(nb_words=5))


class PhotoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Photo

    photographer = factory.SubFactory(UserFactory)

    file = factory.django.ImageField(color='red')
    height_field = 100
    width_field = 100


class ModelTestCases(TestCase):

    def setUp(self):
        self.user = UserFactory.create()
        self.client.force_login(user=self.user)
        self.album = AlbumFactory(photographer=self.user)
        self.today = datetime.date.today()

    def test_album(self):
        self.album = AlbumFactory(photographer=self.user)
        # self.user = self.album.user.photographer
        # import pdb; pdb.set_trace()
        self.client.force_login(user=self.user)
        self.assertTrue(self.album.published == 'private')
        self.assertTrue(type(self.album.title) == str)
        self.assertEqual(self.album.date_created, self.today)
        self.assertEqual(self.album.date_modified, self.today)
        self.assertEqual(self.album.date_pub, None)
        self.assertEqual(self.album.cover_photo, '')
        self.assertTrue(self.album.description is not None)

    def test_album_many_photos(self):
        self.album.photos.add(*PhotoFactory.create_batch(5, photographer=self.user))
        import pdb; pdb.set_trace()
        self.assertTrue('dog' == 'cat')

    def test_photo(self):
        self.photo = PhotoFactory(photographer=self.user)
        # self.client.force_login(user=self.user)
        # import pdb; pdb.set_trace()
        self.assertTrue(self.photo.photographer.username == self.user.username)




















########
