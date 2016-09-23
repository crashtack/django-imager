from django.conf.urls import include, url
from imager_profile.models import Photographer
from django.views.generic import DetailView, TemplateView


# urlpatterns = [
#     url(r'^(?P<user_uuid>[a-f|0-9|-]+)$', DetailView.as_view(
#         template_name="imager_profile/profile.html",
#         model=Photographer,
#         pk_url_kwarg='user_uuid')),
# ]

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="imager_profile/profile.html"), name="personal_profile"),
    url(r'^(?P<user_uuid>[a-f|0-9|-]+)$', DetailView.as_view(
        template_name="imager_profile/public_profile.html",
        model=Photographer,
        pk_url_kwarg='user_uuid',
        context_object_name="photographer"
        )),
]
