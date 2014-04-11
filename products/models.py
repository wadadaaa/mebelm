from django.db import models
from django.core.urlresolvers import reverse_lazy as reverse




class Catalog(models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children')
    image = models.ImageField(upload_to="category_pic", blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('catalog_detail', kwargs={'slug': self.slug})


class Product(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    image = models.ImageField(upload_to='product_images', blank=True, null=True)
    catalog = models.ForeignKey(Catalog)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    sale_price = models.DecimalField(max_digits=15, decimal_places=2)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return reverse('product_detail', [str(self.slug)])
        #return reverse('product_detail', kwargs={'slug': self.slug})
        return '/products/view/%s' % self.slug


    # def get_absolute_url(self):
    #     #return reverse('product_detail', [str(self.slug)])
    #     #return ('product_detail', [self.slug,])
    #     #return reverse('product_detail', kwargs={'slug': self.slug})
    #     #return reverse('product_detail', args=[str(self.slug)])
    #     return '/products/view/%s' % self.slug


