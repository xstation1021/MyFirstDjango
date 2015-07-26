from django.db import models
from django.utils import timezone
from ingredient.models import Ingredient

class Product(models.Model):
    ingredient_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    brand = models.CharField(max_length=50, blank=True, null=True)
    measure = models.CharField(max_length=50, blank=True, null=True)
    unit_size = models.CharField(max_length=11, blank=True, null=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    ingredient = models.OneToOneField(Ingredient, to_field='id', related_name='ingredient_profile')

    class Meta:
        managed = False
        db_table = 'products'
        
    def create(self):
        self.created_at = timezone.now()
        self.save()

    def update(self):
        self.updated_at = timezone.now()
        self.save()