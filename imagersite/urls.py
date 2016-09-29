"""imagersite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from imagersite.views import home_view
from django.contrib.auth.views import logout


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home_view, name='homepage'),
    url(r'^logout/$', logout, {'next_page': '/'}),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^profile/', include('imager_profile.urls')),
    url(r'^images/', include('imager_images.urls')),

]

"""
    Other active Routes:
        login/ -----------------------> /registration/login.html
        accounts/register/ -----------> /registration/registration_form.html
        accounts/register/complete/ --> /registration/registration_complete.html
        accounts/register/closed/ ----> /registration/registration_closed.html
        accounts/activate/complete/ --> /registration/activation_complete.html
        url(r'^activate/(?P<activation_key>[-:\w]+)/$',
                views.ActivationView.as_view(),
                name='registration_activate')  -----> /nowhere yet.
"""

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
