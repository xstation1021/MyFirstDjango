from rest_framework import serializers
from product.models import Product

class ProductSerializer(serializers.ModelSerializer):

	class Meta:
		model = Product
		fields = ('id', 'name', 'brand', 'measure', 'unit_size', 'unit_price', 'category_id', 'ingredient_id', 'ingredient')