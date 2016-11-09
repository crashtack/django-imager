from django.conf.urls import include, url
from imager_profile.models import Photographer
from django.views.generic import DetailView, TemplateView
from imager_images.views import library_view
from imager_images.views import UploadPhotoView, AddAlbumView, EditPhoto
from imager_images.views import EditAlbumView
from imager_images.models import Photo, Album


urlpatterns = [
    url(r'^library/$',
        library_view,
        name="personal_library"),

    url(r'^album/add/$',
        AddAlbumView.as_view(),
        name='add_album'
        ),

    url(r'^album/(?P<pk>[0-9]+)$',
        DetailView.as_view(
            template_name="imager_images/album.html",
            model=Album,
            # pk_url_kwarg='id',
            context_object_name="album",
        ),
        name='album'),

    url(r'^photos/add/$',
        UploadPhotoView.as_view(),
        name='upload_photo',
        ),

    url(r'^photos/(?P<photo_id>[a-f|0-9|-]+)$',
        DetailView.as_view(
            template_name="imager_images/photo.html",
            model=Photo,
            pk_url_kwarg='photo_id',
            context_object_name="photo",
        ),
        name='photo'),

    url(r'^photos/(?P<photo_id>[a-f|0-9|-]+)/edit/$',
        EditPhoto.as_view(
            template_name="imager_images/edit_photo.html",
            model=Photo,
            pk_url_kwarg='photo_id',
            context_object_name="photo",
        ),
        name='edit_photo'),

    url(r'^album/(?P<pk>[0-9]+)/edit/$',
        EditAlbumView.as_view(),
        name='edit_album'
        ),
]
