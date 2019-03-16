from django.http import HttpResponseRedirect
from django_mako_plus import view_function, jscontext
from catalog import models as cmod
from django import forms



###################################
### Product detail page

@view_function
def process_request(request, product:cmod.Product):
    print(product)
    return request.dmp.render('product.html', {
        'product': product,
    })
    


###################################
### Product tile ajax endpoint


@view_function
def tile(request, product:cmod.Product):
    return request.dmp.render('product.tile.html', {
        'product': product,
    })