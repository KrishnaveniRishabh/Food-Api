from django.db import models

class FoodRecipe(models.Model):
    FOOD_TYPE_CHOICES = [
        ('VEG', 'Vegetarian'),
        ('NON-VEG', 'Non-Vegetarian'),
    ]

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    ingredients = models.TextField()
    method = models.TextField()
    category = models.CharField(max_length=10, choices=FOOD_TYPE_CHOICES)



    def __str__(self):

        return self.name