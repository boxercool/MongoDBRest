from rest_framework.routers import DefaultRouter
from django.urls import path,include

from CookingApi.views import RecipeView, IngredientView, CookerCRUD, CookerView

router = DefaultRouter()

router.register(r'ingredients', IngredientView)
router.register(r'recipes', RecipeView)
router.register(r'cooker', CookerView)

urlpatterns = [
    path('Cook/',include(router.urls)),
    path('cooker/id/<int:pk>', CookerCRUD.as_view(), name='cooker')



]