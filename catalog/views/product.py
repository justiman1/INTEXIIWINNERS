from django_mako_plus import view_function, jscontext
from catalog import models as cmod



###################################
### Product tile ajax endpoint


@view_function
def tile(request, product:cmod.Product):
    return request.dmp.render('product.tile.html', {
        'product': product,
    })