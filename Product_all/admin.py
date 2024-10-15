from django.contrib import admin
from .models import *
# Register your models here.
class ProductAdd(admin.ModelAdmin):
    list_display=('product_name', 'product_price', 'category', 'product_image')

admin.site.register(Product_add, ProductAdd)
