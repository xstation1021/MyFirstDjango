from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Product
from product.serializers import ProductSerializer
from django.db import connection

@api_view(['GET'])
def product_collection(request):
    if request.method == 'GET':
        
        cursor = connection.cursor()

        cursor.execute("SELECT p.*, c.name as cname, i.name as iname FROM products p JOIN ingredients i ON i.id = p.ingredient_id JOIN categories c ON c.id = p.category_id")
        row = dictfetchall(cursor)
        
        return Response(row)

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]        

@api_view(['GET'])
def product_element(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

@api_view(['POST'])
def product_create(request):
    if request.method == 'POST':

        data = {'name': request.DATA.get('name'), 
        'brand': request.DATA.get('brand'), 
        'measure': request.DATA.get('measure'), 
        'unit_size': request.DATA.get('unit_size'), 
        'unit_price': request.DATA.get('unit_price'), 
        'category_id': request.DATA.get('category_id'), 
        'ingredient_id': request.DATA.get('ingredient_id'), 
        }  

        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)