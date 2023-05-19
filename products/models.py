from django.db import models
from django.utils.translation import gettext as _

from ckeditor.fields import RichTextField


class ProductModel(models.Model):
    title = models.CharField(_('Title'), max_length=50)
    description = RichTextField(_('Description', ))
    short_description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    cover = models.ImageField(upload_to='covers')

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
