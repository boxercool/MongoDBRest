"""MongoDBRest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from App1.views import sayHello,home,viewHtml
from ExamApi.views import   MobileProductViewset,MusicianListView,AlbumListView,MusicianView,AlbumView,PlaceListView,PlaceView,UseListView,UseView,HomeListView,HomeView,ShopItemListView,ShopItemView
from Employee import views
from MusicApp.views import *


from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('musician1', MusicianViewset, basename='musician')
router.register('album', AlbumViewset, basename='album')
router.register('place', PlaceViewset, basename='place')
router.register('use', UseViewset, basename='use')
router.register('home', HomeViewset, basename='home')
router.register('mobile',MobileProductViewset,basename='mobile')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('Home/',sayHello),
    path('Welcome/',home),
    path('index/',viewHtml),
   

    path('',include('Api_Basic.urls')),
    #path('',include('CookingApi.urls')),
  #  path(r'^path/to/API/', include('rest_framework.urls', namespace='widget-api')),
   # path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('',include('Question_Api.urls')),
    path('post/',include('Post_Api.urls')),

     path('', include(router.urls)),


    # Multi Level Nested Url
    path('api/musicians/', MusicianListView.as_view()),
    path('api/musicians/<int:pk>/', MusicianView.as_view()),
    path('api/albums/', AlbumListView.as_view()),
    path('api/albums/<int:pk>/', AlbumView.as_view()),
    path('api/place/',PlaceListView.as_view()),
    path('api/place/<int:pk>/',PlaceView.as_view()),
    path('api/use/',UseListView.as_view()),
    path('api/use/<int:pk>/', UseView.as_view()),
    path('api/demo/', HomeListView.as_view()),
    path('api/demo/<int:pk>/', HomeView.as_view()),
    path('api/shop/', ShopItemListView.as_view()),
    path('api/shop/<int:pk>/', ShopItemView.as_view()),


    path('emp', views.emp),
    path('show', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy)

    #path('api/polls/', include('polls.urls'))
   # path('api/v1',include('App1.api_url')),
    #path(r'^polls/', include('polls.urls')),
]
