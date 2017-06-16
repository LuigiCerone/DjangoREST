from django.conf.urls import url, include
from rest_framework import routers

from Photo.views import PhotoViewSet, AlbumViewSet
from . import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'photo', PhotoViewSet, base_name='photo')
router.register(r'album', AlbumViewSet)

app_name = 'Photo'
urlpatterns = [
    url(r'^', include(router.urls)),
]

