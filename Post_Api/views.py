from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Posts, PostsRates
from .serializer import PostsSerializer, PostsRatesSerializer


class PostsViewSet(viewsets.ModelViewSet):
    serializer_class = PostsSerializer

    def get_queryset(self):
        posts = Posts.objects.all()
        return posts

    def create(self, request, *args, **kwargs):
        post_data = request.data

        new_rate = PostsRates.objects.create(
            likes=post_data["rates"]["likes"], dislikes=post_data["rates"]["dislikes"])
        new_rate.save()

        new_post = Posts.objects.create(
            post_title=post_data["post_title"], post_body=post_data["post_body"], rates=new_rate)
        new_post.save()

        serializer = PostsSerializer(new_post)

        return Response(serializer.data)

    '''
    posts = Posts.objects.all()
    serializer_class = PostsSerializer

    def retrieve(self, request, *args, **kwargs):
        # do your customization here
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data) '''


class PostsRatesViewSet(viewsets.ModelViewSet):
    serializer_class = PostsRatesSerializer

    def get_queryset(self):
        rates = PostsRates.objects.all()
        return rates

