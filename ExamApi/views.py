from django.shortcuts import render
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from django.http import Http404
from rest_framework import status

from rest_framework.response import Response


class MusicianListView(generics.ListCreateAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class MusicianView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MusicianSerializer
    queryset = Musician.objects.all()


class AlbumListView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()

class PlaceListView(generics.ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
class  PlaceView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()

class UseListView(generics.ListCreateAPIView):
    queryset = Use.objects.all()
    serializer_class = UseSerializer

class  UseView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UseSerializer
    queryset = Use.objects.all()

class HomeListView(generics.ListCreateAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer

class  HomeView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UseSerializer
    queryset = Home.objects.all()


class ShopItemListView(generics.ListCreateAPIView):
    queryset = ShopItem1.objects.all()
    serializer_class = ShopItemSerializer
    lookup_field = id
    def create(self, request, *args, **kwargs):
        mymodel=None
        id=request.data.get("name")
        if id:
            print(mymodel)
            mymodel=request.data['name']
            print(mymodel)

        if mymodel:
            return self.update(request, *args, **kwargs)
        else:
            return self.create(request, *args, **kwargs)

'''
    def create(self, request):
       # da=request.data['id']
        #print(da)
       # va= ShopItem1.objects.get(id=ShopItem1_id)
        #print(va)

        name=request.data['name']

        attrs=request.data['attrs']
        myModel, created = ShopItem1.objects.update_or_create(name=name,
                                                           defaults={
                                                             attrs: attrs
                                                           })

        print(myModel.name)
        # require context={'request': request} because i'm using HyperlinkModelSerializer
        serializer = ShopItemSerializer(myModel, data=request.data, context={'request': request})
        if serializer.is_valid():
            print(serializer)
            serializer.save()


        elif created:
            return Response(serializer.data, status.HTTP_201_CREATED)
            print('elif')
        else:
            return Response(serializer.data, status.HTTP_200_OK)
            print('else')

'''

'''
    def perform_create(self, serializer):
        if serializer.is_valid():
            name = serializer.validated_data['name']
            print(name)


            if name != '':
                product_list = ShopItem1.objects.filter(
                    name=name,)
                print(product_list)

                if not product_list:
                    product = serializer.save()
                else:
                    product = product_list[0]
                    serializer = ShopItemSerializer(product)
                return Response(serializer.data)
            else:
                return Response(data={'message': 'Empty product_name'},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
class  ShopItemView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShopItemSerializer
    queryset = ShopItem1.objects.all()

'''
    def create(self, request,ShopItem1_id):
       # da=request.data['id']
        #print(da)
        va= ShopItem1.objects.get(id=ShopItem1_id)
        print(va)
        myModel, created = ShopItem1.objects.update_or_create(name=request.data['name'],
                                                           defaults={
                                                             'name': request.data['name']
                                                           })

        # require context={'request': request} because i'm using HyperlinkModelSerializer
        serializer = ShopItemSerializer(myModel, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()

        if created:
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status.HTTP_200_OK)
'''

from rest_framework import viewsets
import json

class MobileProductViewset(viewsets.ModelViewSet):
    serializer_class = MobileProductSerializer

    def get_queryset(self):
        queryset = MobileProduct.objects.all()
        
        return queryset

    def create(self, request, *args, **kwargs):
        data = request.data
        value=MobileProduct.objects.all()
        print('First Value',value.first())
        Checkdata = MobileProduct.objects.filter(Productid=request.data['Productid']).exists()
        savevalue=request.data['Productid']
       # print(Checkdata)
        if Checkdata:
            mobile = MobileProduct.objects.filter(Productid=request.data['Productid'])
         #   print(mobile)
            mobile.delete()
            mobile = MobileProduct.objects.create(Productid=savevalue ,Productname=data['Productname'], Productdetails=data['Productdetails'])

            mobile.save()
        else:
            mobile = MobileProduct.objects.create(Productid=data['Productid'], Productname=data['Productname'],
                                                  Productdetails=data['Productdetails'])

            mobile.save()

        cdata=json.load(MobileProductSerializer(mobile).data)
        return Response(cdata)

    def update(self, request, *args, **kwargs):
        data = request.data
       # print('Mobile Data',data)
        mobile = self.get_object()

        mobile.Productid = data['Productid']
        mobile.Productname = data['Productname']
        mobile.Productdetails = data['Productdetails']

        mobile.save()
        jdata=json.load(MobileProductSerializer(mobile).data)
        return Response(jdata)

    def destroy(self, request, *args, **kwargs):
        mobile = self.get_object()
        mobile.delete()

        return Response({'message': 'Mobile object has been deleted'})




