"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [     
	url(r'^$', 'home.views.index'),   
	url(r'^api/recipes/$', 'recipe.views.recipe_collection'),
    url(r'^api/recipes/add', 'recipe.views.recipe_create'),
    url(r'^api/recipes/update', 'recipe.views.recipe_update'),
	url(r'^api/recipes/(?P<pk>[0-9]+)$', 'recipe.views.recipe_element'),
    url(r'^api/search/recipes/(?P<search>.*)', 'recipe.views.recipe_search_collection'),
    
    url(r'^api/ingredients/$', 'ingredient.views.ingredient_collection'),
    url(r'^api/ingredients/(?P<pk>[0-9]+)$', 'ingredient.views.ingredient_element'),
    url(r'^api/ingredients/add', 'ingredient.views.ingredient_create'),
    
    url(r'^api/products/$', 'product.views.product_collection'),
    url(r'^api/products/(?P<pk>[0-9]+)$', 'product.views.product_element'),
    url(r'^api/products/add', 'product.views.product_create'),
    
    url(r'^api/categories/$', 'category.views.category_collection'),
    url(r'^api/categories/(?P<pk>[0-9]+)$', 'category.views.category_element'),
    url(r'^api/categories/add', 'category.views.category_create'),

    url(r'^admin/', include(admin.site.urls)),
]
