from django.utils.timezone import now
from django.views.generic import ListView, DetailView


from .models import (
    Product,
    Catalog,
)


class ProductsList(ListView):
    model = Product
    context_object_name = 'products'


class ProductDetail(DetailView):
    model = Product
    context_object_name = 'product'


class CatalogList(ListView):
    model = Catalog
    context_object_name = 'catalogs'





