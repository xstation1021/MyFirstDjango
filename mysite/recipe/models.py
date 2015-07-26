from django.db import models
from django.utils import timezone

class Recipe(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)
    prep_time = models.CharField(max_length=50, blank=True, null=True)
    cook_time = models.CharField(max_length=50, blank=True, null=True)
    serving_size = models.CharField(max_length=50, blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)
    code = models.CharField(max_length=50, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'recipes'

    def create(self):
        self.created_at = timezone.now()
        self.save()

    def update(self):
        self.updated_at = timezone.now()
        self.save()    


class RecipeIngredients(models.Model):
    unit = models.IntegerField(blank=True, null=True)
    ingredient_id = models.IntegerField(blank=True, null=True)
    recipe_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recipe_ingredients'

    def create(self):
        self.created_at = timezone.now()
        self.save()

    def update(self):
        self.updated_at = timezone.now()
        self.save()  