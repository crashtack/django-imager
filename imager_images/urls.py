from django.conf.urls import include, url
from imager_profile.models import Photographer
from django.views.generic import DetailView, TemplateView
from imager_images.views import library_view
from imager_images.views import UplaodPhotoView
from imager_images.models import Photo, Album


urlpatterns = [
    url(r'^library/$',
        library_view,
        name="personal_library"),

    url(r'^photos/(?P<photo_id>[a-f|0-9|-]+)$',
        DetailView.as_view(
            template_name="imager_images/photo.html",
            model=Photo,
            pk_url_kwarg='photo_id',
            context_object_name="photo",
        ),
        name='photo'),

    url(r'^album/(?P<id>[a-f|0-9|-]+)$',
        DetailView.as_view(
            template_name="imager_images/album.html",
            model=Album,
            pk_url_kwarg='id',
            context_object_name="album",
        ),
        name='album'),

    url(r'^photos/new/$',
        UplaodPhotoView.as_view(),
        name='upload_photo',
        )
]
