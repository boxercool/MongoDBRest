from django.contrib import admin
from django.urls import path,include
from App1.views import *
from rest_framework import routers

router=routers.DefaultRouter()
router.register('employee',EmployeeViewSet)

urlpatterns = [
    path('employee',include(router.urls)),

]
