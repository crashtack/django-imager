from django.conf.urls import url, include
from imager_api import views
from rest_framework.routers import DefaultRouter


# Create a router and register or viewsets with it
router = DefaultRouter()
router.register(r'photos', views.PhotoViewSet)
router.register(r'albums', views.AlbumViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determinded automatically by the router.
# Additianally, we include the login Urls for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/',
        include('rest_framework.urls',
                namespace='rest_framework'
                )
        )
]


# Login and logout views for the browsable API
# urlpatterns += [
#     url(r'^api-auth/', include('rest_framework.urls',
#                                namespace='rest_framework')),
# ]
