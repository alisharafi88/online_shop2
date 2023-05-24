from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from ckeditor.fields import RichTextField


class CategoryModel(models.Model):
    master_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='master', null=True, blank=True)
    title = models.CharField(_('Title'), max_length=50)
    description = RichTextField(_('Description', ), blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        full_path = [self.title]
        k = self.master_category
        while k is not None:
            full_path.append(k.title)
            k = k.master_category

        return ' -> '.join(full_path[::-1])

    # def __str__(self):
    #     return self.title
    #

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

    def __str__(self):
        return f'{self.title}:{self.price}'

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])



class CommentModel(models.Model):
    COMMENT_CHOICES = [
        ("1", _('very bad')),
        ("2", _('bad')),
        ("3", _('normal')),
        ("4", _('good')),
        ("5", _('very good')),
    ]
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments',)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='comments',)
    text = models.TextField(verbose_name=_("text"))
    point = models.CharField(max_length=10, choices=COMMENT_CHOICES, verbose_name=_('point'))
    active = models.BooleanField(default=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.user.nick_name:
            return self.user.nick_name
        return self.user.first_name

