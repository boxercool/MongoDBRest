from django.shortcuts import render
from .serializers import BookSerializer,BookDetailsSerializer
from rest_framework.response import Response
from  rest_framework  import status
from rest_framework.views import APIView

# Create your views here.

class BookView(APIView):
    def post(self,request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
