from django.shortcuts import render
from rest_framework import  viewsets
from django.contrib.auth.models import User
from App1.serializers import EmployeeSerializer

# Create your views here.
from django.http import HttpResponse

def sayHello(request):
    return HttpResponse("Welcome Django test Method")


def home(request):
    return HttpResponse("This is Second Test Method")


def viewHtml(request):
    return  render(request,'Hello.html',{'name':'Vijay'})


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = EmployeeSerializer
