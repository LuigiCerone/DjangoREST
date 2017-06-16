# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Photo, Album
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'albumId', 'title', 'url', 'thumbnailUrl')

# ViewSets define the view behavior.
class PhotoViewSet(viewsets.ModelViewSet):
    serializer_class = PhotoSerializer

    def get_queryset(self):
        queryset = Photo.objects.all()
        id = self.request.query_params.get('albumId', None)
        if id is not None:
            queryset = queryset.filter(albumId__in=id)
        return queryset

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'title')

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer