from rest_framework import serializers
from recipe.models import Recipe

class RecipeSerializer(serializers.ModelSerializer):

	class Meta:
		model = Recipe
		fields = ('id', 'name', 'prep_time', 'cook_time', 'serving_size', 'instructions', 'code')


