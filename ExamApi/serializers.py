from ExamApi.models import Album,Musician,Place,Use,Home,ShopItem1,MobileProduct
from rest_framework import serializers#, fields


from Post_Api import serializer


class ShopItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=ShopItem1
        fields=('id','name','attrs')

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Home
        fields=('id','Duse','Dname','Age')
class UseSerializer(serializers.ModelSerializer):
    Demo_Use = HomeSerializer(many=True)

    class Meta:
        model = Use
        fields = ('id', 'pluse', 'Cameramodel', 'byyear', 'Demo_Use')
class PlaceSerializer(serializers.ModelSerializer):
    use_place = UseSerializer(many=True)
    class Meta:
        model=Place
        fields=('id','alname','placename','time','use_place')
'''
        def create(self, validated_data):
            uses_data = validated_data.pop('use_place')
            places = Place.objects.create(**validated_data)
            for use_data in uses_data:
                Use.objects.create(pluse=places, **use_data)
            return places

        def update(self, instance, validated_data):
            uses_data = validated_data.pop('use_place')
            print(uses_data)
            uses = (instance.use_place).all()
            uses = list(uses)
            instance.placename = validated_data.get('placename', instance.placename)
            instance.time = validated_data.get('time', instance.time)

            instance.save()

            for use_data in uses_data:
                use = uses.pop(0)
                use.placename = use_data.get('placename', use.placename)
                use.time = use_data.get('time', use.time)

                use.save()
            return instance

'''
class AlbumSerializer(serializers.ModelSerializer):
   place_album=PlaceSerializer(many=True)

   class Meta:
       model = Album
       fields = ('id', 'artist', 'name', 'release_date', 'num_stars', 'place_album')

   '''
   def create(self, validated_data):
        place_data = validated_data.pop('place_album')
        albums = Album.objects.create(**validated_data)
        for place_data in place_data:
            Place.objects.create(alname=albums, **place_data)
        return albums
   def update(self, instance, validated_data):
        place_data = validated_data.pop('place_album')
        place = (instance.place_album).all()
        place = list(place)
        instance.artist = validated_data.get('artist', instance.artist)
        instance.name = validated_data.get('name', instance.name)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.num_stars = validated_data.get('num_stars', instance.num_stars)
        instance.save()
        for plac_data in place_data:
            places = place.pop(0)
            places.alname = plac_data.get('alname', places.alname)
            places.placename = plac_data.get('placename', places.placename)
            places.time = plac_data.get('time', places.time)

            places.save()
        return instance

'''



class MusicianSerializer(serializers.ModelSerializer):
    album_musician = AlbumSerializer(many=True)

    class Meta:
        model = Musician
        fields = ('id', 'first_name', 'last_name', 'instrument', 'album_musician')
     #   lookup_field=id

    def create(self, validated_data):
        albums_data = validated_data.pop('album_musician')
        musician = Musician.objects.create(**validated_data)
        for album_data in albums_data:
            Album.objects.create(artist=musician, **album_data)
        return musician

    def update(self, instance, validated_data):
        albums_data = validated_data.pop('album_musician')
        albums = (instance.album_musician).all()
        albums = list(albums)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.instrument = validated_data.get('instrument', instance.instrument)
        instance.save()

        for album_data in albums_data:
            album = albums.pop(0)
            album.name = album_data.get('name', album.name)
            album.release_date = album_data.get('release_date', album.release_date)
            album.num_stars = album_data.get('num_stars', album.num_stars)
            album.save()
        return instance
'''
    def update(self, instance, validated_data):
        place_data = validated_data.pop('place_album')
        places=(instance.place_album).all()
        places=list(places)
        instance.placename=validated_data.get('placename',places.placename)

        return instance
'''

'''

    def update(self, instance, validated_data):
        albums_data = validated_data.pop('album_musician')
        place_data = validated_data.get('place_album')
        albums = (instance.album_musician).all()
        albums = list(albums)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.instrument = validated_data.get('instrument', instance.instrument)
        instance.save()





        for album_data in albums_data:

            place1=(albums.place_album).all()
           # place1=list(place1)
            album = albums.pop(0)

            album.name = album_data.get('name', album.name)
            album.release_date = album_data.get('release_date', album.release_date)
            album.num_stars = album_data.get('num_stars', album.num_stars)
            album.save()
            for place_data in place_data:
                place1=place1.pop(0)
                place1.placename=place_data.get('placename',place1.placename)
                place1.time=place_data.get('time',place1.time)
                place1.save()
        return instance
        '''
'''
    for album_data in albums_data:
        album = albums.pop(0)
        print('the value', album)
        album.name = album_data.get('name', album.name)
        album.release_date = album_data.get('release_date', album.release_date)
        album.num_stars = album_data.get('num_stars', album.num_stars)
        album.save()
    return instance

'''

class MobileProductSerializer(serializers.ModelSerializer):

    class Meta:
        model =MobileProduct
        fields = ( 'Productid', 'Productname', 'Productdetails')
