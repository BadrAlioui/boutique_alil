from django.contrib import admin
from .models import Category, Product, Order

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'brand', 'price', 'rating', 'image']
    

admin.site.register(Category, CategoryAdmin)

admin.site.register(Product, ProductAdmin)

admin.site.register(Order)

    