from django.conf.urls import url
from imager_profile.views import profile_view, EditProfileView


urlpatterns = [
    url(r'^$',
        profile_view,
        name="private_profile"),

    url(r'^edit/$',
        EditProfileView.as_view(),
        name='edit_profile'
        ),

]
