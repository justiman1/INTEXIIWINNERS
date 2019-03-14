from django.conf import settings
from django_mako_plus import view_function, jscontext
from catalog import models as cmod
import math


ITEMS_PER_PAGE = 8


@view_function
def process_request(request, category:cmod.Category=None, page:int=1):
    products = cmod.Product.objects.all()
    if category is not None:
        products.filter(category=category)

    products = products[(page - 1) * ITEMS_PER_PAGE: page * ITEMS_PER_PAGE]

    return request.dmp.render('index.html', {
        'category': category,
        'products': products,
        'page': page,
        'numpages': math.ceil(products.count() / ITEMS_PER_PAGE),
    })
