from django.db import models
from django.utils import timezone

class Ingredient(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    measure = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingredients'

    def create(self):
        self.created_at = timezone.now()
        self.save()

    def update(self):
        self.updated_at = timezone.now()
        self.save()     