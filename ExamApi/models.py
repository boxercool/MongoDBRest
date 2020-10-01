

# Create your models here.
from django.db import models
#from django.contrib.postgres.fields import JSONField

# Create your views here.
from jsonfield import JSONField
import uuid


class Musician(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def __unicode__(self):
        return self.first_name


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name='album_musician', null=True, blank=True)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()


class Place(models.Model):
    alname=models.ForeignKey(Album,on_delete=models.CASCADE,related_name='place_album',null=True,blank=True)
    placename=models.CharField(max_length=50)
    time=models.CharField(max_length=50)

class Use(models.Model):
    pluse=models.ForeignKey(Place,on_delete=models.CASCADE,related_name='use_place',null=True,blank=True)
    Cameramodel=models.CharField(max_length=50)
    byyear=models.DateField()

class Home(models.Model):
    Duse=models.ForeignKey(Use,on_delete=models.CASCADE,related_name='Demo_Use',null=True,blank=True)
    Dname=models.CharField(max_length=50)
    Age=models.IntegerField()

class ShopItem1(models.Model):
   # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    attrs = JSONField()

class Voter(models.Model):
    BaseProductID = models.CharField(max_length=100)

class Vote(models.Model):
    Company = models.CharField(max_length=100)
    Basevalue = models.ForeignKey(Voter, on_delete=models.CASCADE)
    Price=models.IntegerField()

class MobileProduct(models.Model):
   # id = models.AutoField()
    Productid=models.CharField(primary_key=True,max_length=20)
    Productname=models.CharField(max_length=200)
    Productdetails=JSONField()



