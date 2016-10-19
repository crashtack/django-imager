from imager_images.models import Photo, Album
from imager_api.serializers import PhotoSerializer, AlbumSerializer
from imager_api.serializers import UserSerializer
from rest_framework import viewsets, permissions
from imager_api.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User


class PhotoViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update', and 'destroy' actions.
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    lookup_field = 'photo_id'

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AlbumViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update', and 'destroy' actions.
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    # lookup_field = 'photo_id'

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Automatically provides 'list' and 'detail' views
    """
    permissions_classes = (permissions.IsAuthenticated)
    queryset = User.objects.all()
    serializer_class = UserSerializer
