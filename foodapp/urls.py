from django.urls import path
from . import views 
app_name = 'foodapp'
urlpatterns = [
    path('recipes/',views.FoodRecipeListAPIView.as_view(), name='food-recipe-list'),
    path('recipes/create/',views.FoodRecipeCreateAPIView.as_view(), name='food-recipe-create'),
    path('recipes/<int:pk>/',views.FoodRecipeUpdateAPIView.as_view(), name='food-recipe-update'),
]