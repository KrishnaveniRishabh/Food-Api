
# foodapp/views.py
from rest_framework import generics
from .models import FoodRecipe
from .serializer import FoodRecipeSerializer

class FoodRecipeListAPIView(generics.ListAPIView):
    serializer_class = FoodRecipeSerializer

    def get_queryset(self):
        food_type = self.request.query_params.get('food_type', None)
        if food_type:
            return FoodRecipe.objects.filter(category=food_type)
        return FoodRecipe.objects.all()

class FoodRecipeCreateAPIView(generics.CreateAPIView):
    serializer_class = FoodRecipeSerializer

class FoodRecipeUpdateAPIView(generics.UpdateAPIView):
    serializer_class = FoodRecipeSerializer
    queryset = FoodRecipe.objects.all()

