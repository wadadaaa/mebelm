from django.conf.urls import patterns, url
from products.views import ProductsList, ProductDetail, CatalogList
from django.views.generic import ListView, DetailView
from .models import Product

urlpatterns = patterns('',
    url(r'^$', ProductsList.as_view(), name='products_list'),
    #url(r'^$', ProductDetail.as_view(), name='product_detail'),
    #url(r'^view/(?P<pk>\d+)/$', ProductDetail.as_view(), name='product_detail'),
    #url(r'^view/(?P<slug>\w+)/$', ProductDetail.as_view(), name='product_detail'),
    url(r'^view/(?P<slug>[-_\w]+)/$', ProductDetail.as_view(), name='product_detail'),
    #url(r'/view/(?P<slug>[-w]+)/$', ProductDetail.as_view(), name='product_detail'),
    url(r'^catalog/list/$', CatalogList.as_view(), name='catalog_list'),


)