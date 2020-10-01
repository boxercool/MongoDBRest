from django.contrib import admin
from .models import Place,Album,Musician

# Register your models here.
admin.register(Musician)
admin.register(Album)
admin.register(Place)
