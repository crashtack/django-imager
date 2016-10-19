from rest_framework import serializers
from imager_images.models import Photo, Album
from django.contrib.auth.models import User


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    """
     Serialize some photos
    """
    # owner = serializers.ReadOnlyField(source='photograper.username')
    url = serializers.HyperlinkedIdentityField(
        view_name='photo-detail',
        lookup_field='photo_id',
    )

    class Meta:
        model = Photo
        fields = ('url', 'photographer', 'photo_id',
                  'file', 'title', 'description', 'date_created',
                  'date_modified', 'date_pub', 'published')


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    """
     Serialize some photos
    """
    # owner = serializers.ReadOnlyField(source='photograper.username')
    # url = serializers.HyperlinkedIdentityField(
    #     view_name='photo-detail',
    #     lookup_field='photo_id',
    # )

    class Meta:
        model = Album
        fields = ('url', 'photographer', 'title', 'description',
                  'cover_photo', 'date_created', 'date_modified',
                  'published')


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'pk', 'username')
