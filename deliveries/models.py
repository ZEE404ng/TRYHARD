from django.db import models
from django.utils import timezone
# Create your models here.

   


class ProductType(models.Model):
    edible = models.CharField(max_length=255),
    non_edible = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Deliveries(models.Model):
    price = models.IntegerField()
    delivery_cost = models.IntegerField()
    resale_value = models.IntegerField()
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(default=timezone.now)