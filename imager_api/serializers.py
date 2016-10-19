from rest_framework import serializers
from imager_images.models import Photo, albums
from django.contrib.auth.models import User


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    """
     Serialize some photos
    """
    owner = serializers.ReadOnlyField(source='photograper.username')

    class Meta:
        model = Photo
        fields = ('url', 'photographer', 'albums', 'photo_id',
                  'file', 'title', 'description', 'date_created',
                  'date_modified', 'date_pub', 'published')
