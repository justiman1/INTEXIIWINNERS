from django.http import HttpResponseRedirect
from django_mako_plus import view_function, jscontext
from catalog import models as cmod
from account import models as pmod

@view_function
def process_request(request, saleItem:cmod.SaleItem):
    for item in cmod.Product.objects.filter(status='A'):
        item.quantity = 100
        item.save()

    saleItem.status = 'D'
    request.user.get_shopping_cart().recalculate()
    saleItem.save()
    return HttpResponseRedirect('/catalog/cart')