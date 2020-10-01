from rest_framework import  serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields=['id','title','author','email']
       # extra_kwargs = {'email': {'read_only': True, 'required': True}}
        read_only_fields = ['email']







