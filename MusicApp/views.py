
from rest_framework.response import Response
from .models import Album, Musician, Place, Use, Home
from .serializers import *
from rest_framework import viewsets


class MusicianViewset(viewsets.ModelViewSet):
    serializer_class = MusicianSerializer

    def get_queryset(self):

        queryset = Musician.objects.all()

        return queryset

    def create(self, request, *args, **kwargs):
        data = request.data


        musician = Musician.objects.create(
            first_name=data['first_name'], last_name=data['last_name'], instrument=data['instrument'])

        musician.save()

        album = Album.objects.create(artist=musician, name=data['album_musician'][0]['name'],
                                     release_date=data['album_musician'][0]['release_date'], num_stars=data['album_musician'][0]['num_stars'])

        album.save()

        place = Place.objects.create(
            alname=album, placename=data['album_musician'][0]['place_album'][0]['placename'], time=data['album_musician'][0]['place_album'][0]['time'])

        place.save()

        use = Use.objects.create(pluse=place, Cameramodel=data['album_musician'][0]['place_album'][0]['use_place'][0]
                                 ['Cameramodel'], byyear=data['album_musician'][0]['place_album'][0]['use_place'][0]['byyear'])

        use.save()

        home = Home.objects.create(Duse=use, Dname=data['album_musician'][0]['place_album'][0]['use_place'][0]
                                   ['Demo_Use'][0]['Dname'], Age=data['album_musician'][0]['place_album'][0]['use_place'][0]['Demo_Use'][0]['Age'])

        home.save()

        return Response(MusicianSerializer(musician).data)

    def update(self, request, *args, **kwargs):

        data = request.data
        musician = self.get_object()

        musician.first_name = data['first_name']
        musician.last_name= data['last_name']
        musician.instrument = data['instrument']

        musician.save()
        album = Album.objects.get(id=request.data['album_musician'][0]['id'])
        print(data['album_musician'][0]['name'])

        album.name=data['album_musician'][0]['name']
        album.release_date=data['album_musician'][0]['release_date']
        album.num_stars=data['album_musician'][0]['num_stars']
        album.save()
        place=Place.objects.get(id=request.data['album_musician'][0]['place_album'][0]['id'])
        print(place)

        place.placename=data['album_musician'][0]['place_album'][0]['placename']
        place.time=data['album_musician'][0]['place_album'][0]['time']

        place.save()
        use=Use.objects.get(id=request.data['album_musician'][0]['place_album'][0]['use_place'][0]['id'])

        use.Cameramodel=data['album_musician'][0]['place_album'][0]['use_place'][0]['Cameramodel']
        use.byyear=data['album_musician'][0]['place_album'][0]['use_place'][0]['byyear']

        use.save()
        home=Home.objects.get(id=request.data['album_musician'][0]['place_album'][0]['use_place'][0]['Demo_Use'][0]['id'])

        home.Dname=data['album_musician'][0]['place_album'][0]['use_place'][0]['Demo_Use'][0]['Dname']
        home.Age=data['album_musician'][0]['place_album'][0]['use_place'][0]['Demo_Use'][0]['Age']


        home.save()

        return Response(MusicianSerializer(musician).data)

    def destroy(self, request, *args, **kwargs):

        music = self.get_object()
        music.delete()

        return Response({'message': 'music object has been deleted'})




class AlbumViewset(viewsets.ModelViewSet):
    serializer_class = AlbumSerializer

    def get_queryset(self):
        queryset = Album.objects.all()
        return queryset


    def create(self, request, *args, **kwargs):
        data = request.data
        musician = Musician.objects.get(id=data['artist'])
        album = Album.objects.create(artist=musician, name=data['name'],
                                     release_date=data['release_date'], num_stars=data['num_stars'])

        album.save()
        place = Place.objects.create(
            alname=album, placename=data['place_album'][0]['placename'], time=data['place_album'][0]['time'])

        place.save()

        use = Use.objects.create(pluse=place, Cameramodel=data['place_album'][0]['use_place'][0]
        ['Cameramodel'], byyear=data['place_album'][0]['use_place'][0]['byyear'])

        use.save()

        home = Home.objects.create(Duse=use, Dname=data['place_album'][0]['use_place'][0]
        ['Demo_Use'][0]['Dname'], Age=data['place_album'][0]['use_place'][0]['Demo_Use'][0]['Age'])

        home.save()

        return Response(AlbumSerializer(album).data)

    def update(self, request, *args, **kwargs):

      #  data = super(AlbumViewset, self).update().data
       # print(data)
        data = request.data
        album = self.get_object()
        album.name = data['name']
        album.release_date = data['release_date']
        album.num_stars = data['num_stars']



        album.save()

        place = Place.objects.get(id=request.data['place_album'][0]['id'])
        print(place)
        place.placename =data['place_album'][0]['placename']
        place.time = data['place_album'][0]['time']

        place.save()

        use =Use.objects.get(id=request.data['place_album'][0]['use_place'][0]['id'])
        use.Cameramodel=data['place_album'][0]['use_place'][0]['Cameramodel']
        use.byyear=data['place_album'][0]['use_place'][0]['byyear']
        use.save()
        home=Home.objects.get(id=request.data['place_album'][0]['use_place'][0]['Demo_Use'][0]['id'])
        home.Dname=data['place_album'][0]['use_place'][0]['Demo_Use'][0]['Dname']
        home.Age=data['place_album'][0]['use_place'][0]['Demo_Use'][0]['Age']
        home.save()

        return Response(AlbumSerializer(album).data)



    def destroy(self, request, *args, **kwargs):

        album = self.get_object()
        album.delete()

        return Response({'message': 'album object has been deleted'})


class PlaceViewset(viewsets.ModelViewSet):

    serializer_class = PlaceSerializer

    def get_queryset(self):
        queryset = Place.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        data = request.data
        album=Album.objects.get(id=data['alname'])
        place = Place.objects.create(
            alname=album, placename=data['placename'], time=data['time'])

        place.save()

        use = Use.objects.create(pluse=place, Cameramodel=data['use_place'][0]
        ['Cameramodel'], byyear=data['use_place'][0]['byyear'])

        use.save()

        home = Home.objects.create(Duse=use, Dname=data['use_place'][0]
        ['Demo_Use'][0]['Dname'], Age=data['use_place'][0]['Demo_Use'][0]['Age'])

        home.save()

        return Response(PlaceSerializer(place).data)

    def update(self, request, *args, **kwargs):
        data = request.data
        # data['use_place'][0]['id']
        place = self.get_object()
        place.placename= data['placename']
        place.time = data['time']


        place.save()

        use=Use.objects.get(id=data['use_place'][0]['Demo_Use'][0]['id'])
        print(use)
        use.Cameramodel=data['use_place'][0]['Cameramodel']
        use.byyear=data['use_place'][0]['byyear']
        use.save()
        home=Home.objects.get(id=data['use_place'][0]['Demo_Use'][0]['id'])
        home.Dname=data['use_place'][0]['Demo_Use'][0]['Dname']
        home.Age=data['use_place'][0]['Demo_Use'][0]['Age']
        home.save()

        return Response(PlaceSerializer(place).data)

    def destroy(self, request, *args, **kwargs):
        place = self.get_object()
        place.delete()

        return Response({'message': 'album object has been deleted'})


class UseViewset(viewsets.ModelViewSet):
    serializer_class = UseSerializer

    def get_queryset(self):
        queryset = Use.objects.all()
        return queryset
    def create(self, request, *args, **kwargs):
        data = request.data

        place=Place.objects.get(id=data['pluse'])

        use = Use.objects.create(pluse=place, Cameramodel=data
        ['Cameramodel'], byyear=data['byyear'])

        use.save()

        home = Home.objects.create(Duse=use, Dname=data
        ['Demo_Use'][0]['Dname'], Age=data['Demo_Use'][0]['Age'])

        home.save()

        return Response(UseSerializer(use).data)

    def update(self, request, *args, **kwargs):
        data = request.data

        use = self.get_object()
        use.Cameramodel= data['Cameramodel']
        use.byyear = data['byyear']


        use.save()
        home =Home.objects.get(id=data['Demo_Use'][0]['id'])
        print('Dname',home)
        home.Dname=data['Demo_Use'][0]['Dname']
        home.Age=data['Demo_Use'][0]['Age']
        home.save()
        return Response(UseSerializer(use).data)

    def destroy(self, request, *args, **kwargs):
        use = self.get_object()
        use.delete()

        return Response({'message': 'album object has been deleted'})



class HomeViewset(viewsets.ModelViewSet):
    serializer_class = HomeSerializer

    def get_queryset(self):
        queryset = Home.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        data = request.data


        use = Use.objects.get(id=data['Duse'])

        home = Home.objects.create(Duse=use, Dname=data
        ['Dname'], Age=data['Age'])

        home.save()

        return Response(HomeSerializer(home).data)

    def update(self, request, *args, **kwargs):
        data = request.data

        home = self.get_object()
        home.Dname = data['Dname']
        home.Age= data['Age']

        home.save()

        return Response(HomeSerializer(home).data)

    def destroy(self, request, *args, **kwargs):
        home = self.get_object()
        home.delete()

        return Response({'message': 'album object has been deleted'})



