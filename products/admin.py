from django.contrib import admin

from .models import ProductModel, CategoryModel


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'active', 'datetime_modified']


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
