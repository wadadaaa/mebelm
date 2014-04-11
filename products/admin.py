from django.contrib import admin

from .models import Product, Catalog

class ProductsAdmin(admin.ModelAdmin):

    class Meta:
        model = Product


class CatalogAdmin(admin.ModelAdmin):

    class Meta:
        model = Catalog

admin.site.register(Product, ProductsAdmin)
admin.site.register(Catalog, CatalogAdmin)

