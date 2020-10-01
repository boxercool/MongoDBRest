from rest_framework import viewsets, generics

from .models import Ingredient, Recipe, Cooker
from .serializers import IngredientSerializer, RecipeSerializer, CookerSerializer

# Based in this question
# http://stackoverflow.com/questions/28078092/django-rest-framework-writable-nested-serializers

class IngredientView(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class RecipeView(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class CookerView(viewsets.ModelViewSet):
    queryset = Cooker.objects.all()
    serializer_class = CookerSerializer

class CookerCRUD(generics.RetrieveUpdateDestroyAPIView):

    queryset = Cooker.objects.all()
    serializer_class = CookerSerializer
