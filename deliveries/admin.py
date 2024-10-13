from django.contrib import admin
from .models import ProductType, Deliveries

class ProductAdmin(admin.ModelAdmin):
    list_display = ('price', 'delivery_cost' )

# class Delivery_Admin(admin.ModelAdmin):
#     list_display = ('edible', 'non_edible')
admin.site.register(ProductType)
admin.site.register(Deliveries, ProductAdmin)
# Register your models here.
