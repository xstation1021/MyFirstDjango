from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ingredient.models import Ingredient
from ingredient.serializers import IngredientSerializer

@api_view(['GET'])
def ingredient_collection(request):
    if request.method == 'GET':
        ingredients = Ingredient.objects.all()
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def ingredient_element(request, pk):
    try:
        ingredient = Ingredient.objects.get(pk=pk)
    except Ingredient.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = IngredientSerializer(ingredient)
        return Response(serializer.data)

@api_view(['POST'])
def ingredient_create(request):
    if request.method == 'POST':

        data = {'name': request.DATA.get('name'), 
        'measure': request.DATA.get('measure'), 
        'quantity': request.DATA.get('quantity'), 
        }  

        serializer = IngredientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)