from rest_framework import serializers
from imager_images.models import Photo, Album
from django.contrib.auth.models import User


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    """
     Serialize some photos
    """
    owner = serializers.ReadOnlyField(source='photograper.username')

    class Meta:
        model = Photo
        fields = ('url', 'owner', 'photographer', 'albums', 'photo_id',
                  'file', 'title', 'description', 'date_created',
                  'date_modified', 'date_pub', 'published')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='user-detail',
        read_only=True,
    )
