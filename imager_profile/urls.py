from django.conf.urls import include, url
from imager_profile.models import Photographer
from django.views.generic import DetailView


urlpatterns = [
    url(r'^(?P<user_uuid>[a-f|0-9|-]+)$', DetailView.as_view(
        template_name="imager_profile/profile.html",
        model=Photographer,
        pk_url_kwarg='user_uuid')),
]
