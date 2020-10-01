
from django.contrib import admin
from django.urls import path,include
from .views import article_list,article_details,ArticleApiView,ArticleDetails,GenericApiView,ArticleViewSet,ArticleModelViewSet

from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('article',ArticleViewSet,basename='article')
router.register('model',ArticleModelViewSet,basename='model')
urlpatterns = [
    path('viewset/',include(router.urls)),
    path('article1/', article_list),
    path('article/',ArticleApiView.as_view()),
    #path('details/<int:pk>/',article_details)
    path('details/<int:id>/',ArticleDetails.as_view()),
    path('Generic/article/<int:id>/',GenericApiView.as_view())
  #  path('modelview/',ArticleModelViewSet.as_view())


]
