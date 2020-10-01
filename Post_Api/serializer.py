from .models import Posts, PostsRates

from rest_framework import serializers


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ["id", "post_title", "post_body", "rates"]
        depth = 1


class PostsRatesSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostsRates
        fields = ["id", "likes", "dislikes"]