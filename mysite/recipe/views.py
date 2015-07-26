from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from recipe.models import Recipe
from recipe.serializers import RecipeSerializer
from django.utils.crypto import get_random_string
from django.db import connection
import json
from recipe.models import RecipeIngredients



def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]   


@api_view(['GET'])
def recipe_collection(request):
    if request.method == 'GET':
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def recipe_search_collection(request, search):
    if request.method == 'GET':
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM recipes r JOIN recipe_ingredients ri ON ri.recipe_id = r.id JOIN ingredients i ON ri.ingredient_id = i.id JOIN products p ON p.ingredient_id = i.id  WHERE i.name = %s OR r.code = %s OR p.name = %s", [search, search, search])
        row = dictfetchall(cursor)
        
        return Response(row)   
   
   

@api_view(['GET'])
def recipe_element(request, pk):
    try:
        recipe = Recipe.objects.get(pk=pk)
    except Recipe.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        cursor = connection.cursor()
        cursor.execute("SELECT ri.id as ri_id, ri.unit, i.id FROM recipe_ingredients ri LEFT JOIN ingredients i ON i.id = ri.ingredient_id WHERE ri.recipe_id = %s", [pk])
        row = dictfetchall(cursor)
        response_data = {}
        response_data['id'] = recipe.id
        response_data['name'] = recipe.name
        response_data['prep_time'] = recipe.prep_time
        response_data['cook_time'] = recipe.cook_time
        response_data['serving_size'] = recipe.serving_size
        response_data['instructions'] = recipe.instructions
        response_data['ingredients'] = row


        serializer = RecipeSerializer(recipe)
        return HttpResponse(json.dumps(response_data), content_type="application/json")


@api_view(['POST'])
def recipe_create(request):
    if request.method == 'POST':

        data = {'name': request.DATA.get('name'), 
        'prep_time': request.DATA.get('name'), 
        'cook_time': request.DATA.get('cook_time'), 
        'serving_size': request.DATA.get('serving_size'), 
        'code': get_random_string(length=8), 
        'instructions': request.DATA.get('instructions')}

        serializer = RecipeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def recipe_update(request):
    if request.method == 'PUT':
        recipe = Recipe.objects.get(pk=request.DATA.get('id'))

        data = {
        'id' : request.DATA.get('id'), 
        'name': request.DATA.get('name'), 
        'prep_time': request.DATA.get('name'), 
        'code' : recipe.code,
        'cook_time': request.DATA.get('cook_time'), 
        'serving_size': request.DATA.get('serving_size'), 
        'instructions': request.DATA.get('instructions')}

        serializer = RecipeSerializer(recipe, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()

            for item in request.DATA.get('ingredients'):
                cursor = connection.cursor()
                print item.has_key('ri_id')
                if item.has_key('ri_id'):
                    cursor.execute("UPDATE recipe_ingredients SET unit = %s, ingredient_id = %s, recipe_id = %s WHERE id = %s", [item['unit'], item['id'], request.DATA.get('id'), item['ri_id']])
                else :
                    cursor.execute("INSERT INTO recipe_ingredients (unit, ingredient_id, recipe_id) VALUES(%s, %s, %s)", [item['unit'], item['id'], request.DATA.get('id')])
                    


            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
