from __future__ import unicode_literals
from django.test import TestCase
import factory
# from faker import Faker
from faker import Factory as FakerFactory
from factory import post_generation, lazy_attribute
from django.contrib.auth.models import User
from imager_images.models import Photo, Album


fake = FakerFactory.create()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "user{}".format(n))
    email = factory.Sequence(
        lambda n: "user{}@example.com".format(n)
    )

    @post_generation
    def albumfactory(self, create, count, **kwargs):
        if count is None:
            count = 3

        make_album = getattr(AlbumFactory, 'create' if create else 'build')
        albums = [make_album(album=self) for i in range(count)]

        if not create:
            '''don't know what this does'''
            self._prefectched_objects_cache = {'album': albums}


class AlbumFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Album

    title = factory.lazy_attribute(lambda o: fake.sentence(nb_words=4))
    description = factory.lazy_attribute(lambda o: fake.sentence(nb_words=35))


class PhotoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Photo

    the_image = factory.django.ImageField(color='red')


class ModelTestCases(TestCase):

    def setUp(self):
        self.user = UserFactory.build()

    def test_add_photo(self):
        self.user.save()
        pass
