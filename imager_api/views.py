from imager_api.models import Photo
from imager_api.serializers import PhotoSerializer
from rest_framwork import viewsets, permissions
from imager_api.permissions import IsOwnerOrReadOnly


class PhotoViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update', and 'destroy' actions.
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (permissions.IsAuthenticatedORReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
