from django.db import models
from django.conf import settings
from django.urls import include, path
from django.contrib.staticfiles.templatetags.staticfiles import static
from decimal import Decimal

# Create your models here.
class Category(models.Model):
    last_modified = models.DateTimeField(null=True, auto_now=True)
    name = models.TextField(null=True)

class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    last_modified = models.DateTimeField(null=True, auto_now=True)
    STATUS_CHOICES = (('A', 'Active'), ('I', 'Inactive'))
    status = models.TextField(db_index=True, choices=STATUS_CHOICES, default='A')
    name = models.TextField(null=True)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField(default=0)
    reorder_trigger = models.IntegerField(default=2)
    reorder_quantity = models.IntegerField(default=5)

    def image_url(self, urls):
    # return an absolute URL to the first image for this product, or if no ProductImage records, the "no image available" image. 
    # The return will be something like: `settings.STATIC_URL + "catalog/media/products/rustic-violin.jpg"`
        if(len(urls) == 0):
            return settings.STATIC_URL + "catalog/media/products/image_unavailable.gif"
        else:
            return self.images_url()[0]
    
    def images_url(self):
    # return a list of absolute URLs to the images for this product, or if no ProductImage records, a list of one item: 
    # the "no image available" image.
        pimages = ProductImage.objects.filter(product=self)
        urls = []
        for p in pimages:
            urls.append(p.image_url())
        if(len(urls) == 0):
            urls.append(settings.STATIC_URL + "catalog/media/products/image_unavailable.gif")
            return urls
        else:
            return urls

class ProductImage(models.Model):
    filename = models.TextField() # example: "violin.jpg"
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')

    def image_url(self):
    # return an absolute URL to this image. 
        return settings.STATIC_URL + "catalog/media/products/" + self.filename


# ************* SPRINT 4 ********************
# Sale Class

class Sale(models.Model):
        user = models.ForeignKey("account.User", on_delete=models.PROTECT)
        created = models.DateTimeField(auto_now_add=True)
        purchased = models.DateTimeField(null=True, default=None)
        subtotal = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
        tax = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
        total = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
        charge_id = models.TextField(null=True, default=None)   # successful charge id from stripe