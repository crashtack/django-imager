from django.conf.urls import include, url
from imager_profile.models import Photographer
from django.views.generic import DetailView, TemplateView
from imager_images.views import library_view
from imager_images.models import Photo


urlpatterns = [
    url(r'^library/$',
        library_view,
        name="personal_library"),
    url(r'^library/photos/(?P<user_uuid>[a-f|0-9|-]+)$',
        DetailView.as_view(
            template_name="imager_images/phto.html",
            model=Photo,
            pk_url_kwarg='photo_id',
            context_object_name="photo",
        ),
        name='photo')

]
