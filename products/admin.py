from django.contrib import admin
from .models import ProductCategory, Product

# Register your models here.

admin.site.register(ProductCategory)
#admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'image', 'description', 'price', 'quantity', 'category')
    search_fields = ('name',)
    ordering = ('name',)
