from django.contrib import admin

from .models import ProductModel, CategoryModel, CommentModel


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'active', 'category', 'datetime_modified']


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'master_category']


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'active']
