from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    birthdate = models.DateTimeField(null=True)
    favcolor = models.TextField(null=True)

    def get_shopping_cart(self):
        from catalog import models as cmod
        cart = cmod.Sale.objects.filter(purchased=None, user=self).first()
        if cart is None:
            cart = cmod.Sale()
            cart.user = self
            cart.save()
        return cart
