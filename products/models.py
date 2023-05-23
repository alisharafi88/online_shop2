from django.db import models
from django.utils.translation import gettext as _

from ckeditor.fields import RichTextField


class CategoryModel(models.Model):
    title = models.CharField(_('Title'), max_length=50)
    description = RichTextField(_('Description', ), blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class ProductModel(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='category', null=False)
    title = models.CharField(_('Title'), max_length=50)
    description = RichTextField(_('Description', ))
    short_description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    cover = models.ImageField(upload_to='covers')
    slug = models.SlugField(unique=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)



