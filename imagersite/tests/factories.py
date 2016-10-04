from __future__ import unicode_literals
import factory
from faker import Factory as FakerFactory
from django.contrib.auth.models import User
from imager_images.models import Photo, Album
from random import randint
from imager_profile.models import Address, Equipment, SocialMedia


fake = FakerFactory.create()


class ValidatedUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = 'bob24'
    email = 'bob24@bob.com'


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "user{}".format(n))
    email = factory.Sequence(
        lambda n: "user{}@example.com".format(n)
    )


class AddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Address

    photographer = factory.SubFactory(UserFactory)
    address_1 = factory.lazy_attribute(lambda o: fake.sentence(nb_words=2))
    city = factory.lazy_attribute(lambda o: fake.sentence(nb_words=1))
    state = 'WA'
    post_code = 1234567


class EquipmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Equipment

    photographer = factory.SubFactory(UserFactory)
    model = factory.lazy_attribute(lambda o: fake.sentence(nb_words=2))


class SocialFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SocialMedia

    photographer = factory.SubFactory(UserFactory)
    url = 'http://fakebook.com/user1234'


class PhotoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Photo

    photographer = factory.SubFactory(UserFactory)
    file = factory.django.ImageField(color='red')
    height_field = 100
    width_field = 100
    title = factory.lazy_attribute(lambda o: fake.sentence(nb_words=2))


class AlbumFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Album

    photographer = factory.SubFactory(UserFactory)
    title = factory.lazy_attribute(lambda o: fake.sentence(nb_words=2))
    description = factory.lazy_attribute(lambda o: fake.sentence(nb_words=5))
    id = randint(1, 99999)
