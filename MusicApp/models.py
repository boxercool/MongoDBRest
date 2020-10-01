from django.db import models

# Create your models here.



# Create your models here.
from django.db import models

# Create your views here.


class Musician(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE,
                               related_name='album_musician', null=True, blank=True)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    def __str__(self):
        return self.name


class Place(models.Model):
    alname = models.ForeignKey(
        Album, on_delete=models.CASCADE, related_name='place_album', null=True, blank=True)
    placename = models.CharField(max_length=50)
    time = models.CharField(max_length=50)

    def __str__(self):
        return self.placename


class Use(models.Model):
    pluse = models.ForeignKey(
        Place, on_delete=models.CASCADE, related_name='use_place', null=True, blank=True)
    Cameramodel = models.CharField(max_length=50)
    byyear = models.DateField()

    def __str__(self):
        return self.Cameramodel


class Home(models.Model):
    Duse = models.ForeignKey(
        Use, on_delete=models.CASCADE, related_name='Demo_Use', null=True, blank=True)
    Dname = models.CharField(max_length=50)
    Age = models.IntegerField()

    def __str__(self):
        return self.Dname


