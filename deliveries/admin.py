from django.contrib import admin
from .models import Product_type, Deliveries

class ProductAdmin(admin.ModelAdmin):
    list_display = ('price', 'delivery_cost', 'resale_value', 'product_type', 'date_ordered' )

admin.site.register(Product_type)
admin.site.register(Deliveries, ProductAdmin)
# Register your models here.
