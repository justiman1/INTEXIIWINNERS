from django.http import HttpResponseRedirect
from django_mako_plus import view_function, jscontext
from catalog import models as cmod
from account import models as amod
from django.conf import settings
from django import forms

@view_function
def process_request(request):
    cart = request.user.get_shopping_cart()
    cart.recalculate()
    SI = cmod.SaleItem.objects.filter(status = 'A', sale = cart)
    

    context = {
        'cart': cart,
        'SI': SI,
    }

    return request.dmp.render('cart.html', context)

# def remove(request, saleitem:cmod.SaleItem):
#     cart = request.user.get_shopping_cart()
#     SI = cmod.SaleItem.objects.filter(status = 'A', sale = cart)
#     for i in SI:
#         if i.product == saleitem:
#             i.status = 'D'

#     SI = cmod.SaleItem.objects.filter(status = 'A', sale = cart)
#     cart.recalculate()
#     cart.save()

#     context = {
#         'cart': cart,
#         'SI': SI,
#     }

#     return request.dmp.render('cart.html', context)



