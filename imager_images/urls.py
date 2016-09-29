from django.conf.urls import include, url
from imager_profile.models import Photographer
from django.views.generic import DetailView, TemplateView
from imager_images.views import library_view


urlpatterns = [
    url(r'^library/$',
        library_view,
        name="personal_library"),
]