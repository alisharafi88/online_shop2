from django.shortcuts import render
from django.views import generic

from .models import ProductModel, CommentModel


class ProductListView(generic.ListView):
    model = ProductModel
    template_name = 'product/product_list.html'
    context_object_name = 'products'


class ProductDetailView(generic.DetailView):
    model = ProductModel
    template_name = 'product/product_detail.html'
    context_object_name = 'product'

    def post(self, request, *args, **kwargs):
        new_comment = CommentModel.objects.create(
            user=self.request.user,
            product=self.get_object(),
            text=self.request.POST.get('text'),
        )
        new_comment.save()
        return self.get(self, request, *args, **kwargs)
