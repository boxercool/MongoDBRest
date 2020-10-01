from .models import Album, Musician, Place, Use, Home
from rest_framework import serializers


class HomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Home
        fields = ('id', 'Duse', 'Dname', 'Age')


class UseSerializer(serializers.ModelSerializer):
    Demo_Use = HomeSerializer(many=True)

    class Meta:
        model = Use
        fields = ('id', 'pluse', 'Cameramodel', 'byyear', 'Demo_Use')


class PlaceSerializer(serializers.ModelSerializer):
    use_place = UseSerializer(many=True)

    class Meta:
        model = Place
        fields = ('id', 'alname', 'placename', 'time', 'use_place')


class AlbumSerializer(serializers.ModelSerializer):
    place_album = PlaceSerializer(many=True)

    class Meta:
        model = Album
        fields = ('id', 'artist', 'name', 'release_date',
                  'num_stars', 'place_album')


class MusicianSerializer(serializers.ModelSerializer):
    album_musician = AlbumSerializer(many=True)

    class Meta:
        model = Musician
        fields = ('id', 'first_name', 'last_name',
                  'instrument', 'album_musician')




