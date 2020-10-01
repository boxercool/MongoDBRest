from .models import Book,BookDetails
from rest_framework import serializers


class BookDetailsSerializer(serializers.ModelSerializer):
   summary = serializers.CharField( max_length=23)
   class Meta:
      model = BookDetails
      fields = ('id', 'summary')

class BookSerializer(serializers.ModelSerializer):
   rbook = BookDetailsSerializer(many=True)

   def create(self, validated_data):
      temp_bok_details= validated_data.pop('rbook')
      new_book = Book.objects.create(**validated_data)
      for i in temp_bok_details:
         BookDetails.objects.create(**i,bok=new_book)
      return new_book
   class Meta:
      model = Book
      fields = ('id','rbook', 'title','author')