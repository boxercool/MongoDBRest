from django.shortcuts import render
from django.http import  HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import ArticleSerializer
from  .models import Article
from django.views.decorators.csrf import csrf_exempt
from  rest_framework.decorators import api_view
from rest_framework.response import Response
from  rest_framework  import status
from rest_framework.views import APIView

from rest_framework import generics
from  rest_framework import mixins
from  rest_framework import viewsets
from django.shortcuts import get_object_or_404
from  rest_framework.filters import SearchFilter,OrderingFilter



class ArticleModelViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields =['title','author']


class ArticleViewSet(viewsets.ViewSet):
    def list(self,request):
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data)

    def create(self,request):
        articles = self.get_object(id)
        serializer = ArticleSerializer(articles, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self,request,pk=None):
        queryset = Article.objects.all()
        article=get_object_or_404(queryset,pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)







class GenericApiView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field ='id'
    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request,id=None):
        return self.update(request,id)

    def delete(self,request,id):
        return self.destroy(request,id)

class ArticleApiView(APIView):
    def get(self,request):
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetails(APIView):
    def get_object(self,id):
        try:
          return  Article.objects.get(id=id)

        except Article.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)



    def get(self,request,id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    

    def put(self,request,id):
        articles = self.get_object(id)
        serializer = ArticleSerializer(articles, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self,request,id):
        articles = self.get_object(id)
        articles.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)



        '''
class ArticleDetails(APIView):

    def get_object(self, id):
        try:
            return Article.objects.get(id=id)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def get(self, request, id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)



    def put(self, request,id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



'''



# Create your views here.
@api_view(['GET','POST'])
def article_list(request):
    if request.method=='GET':
        article=Article.objects.all()
        serializer=ArticleSerializer(article,many=True)
        return Response(serializer.data)

    elif request.method=='POST':
        serializer=ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return  Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def article_details(request,pk):
    try:
        articles=Article.objects.get(pk=pk)

    except Article.DoesNotExist:
        return  HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(articles)
        return Response(serializer.data)



    elif request.method=='PUT':

        serializer = ArticleSerializer(articles,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        articles.delete()

        return  Response(status=status.HTTP_204_NO_CONTENT)


