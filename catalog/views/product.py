from django.http import HttpResponseRedirect
from django_mako_plus import view_function, jscontext
from catalog import models as cmod
from account import models as pmod
from django import forms
import stripe


###################################
### Product detail page

@view_function
def process_request(request, product:cmod.Product):
    if request.method == 'POST':
        
        # Create a form instance and populate it with data from the request (binding):
        form = PurchaseForm(request.POST)
        form.product = product
        form.user = request.user

        if not form.user.is_authenticated:
            return HttpResponseRedirect('/account/login/')
        form.sale = request.user.get_shopping_cart()

        # Check if the form is valid:    
        if form.is_valid():
            sale = request.user.get_shopping_cart()

            query = cmod.SaleItem.objects.filter(sale = sale, product = product)

            if len(query) == 0:
                si = cmod.SaleItem()
                si.status = 'A'
                si.product = product
                si.sale = request.user.get_shopping_cart()
                si.quantity = form.cleaned_data['quantity']
                si.price = product.price * si.quantity
                si.save()
            else:
                query[0].status = 'A'
                query[0].quantity += form.cleaned_data['quantity']
                query[0].price += product.price
                query[0].save()

            return HttpResponseRedirect(f'/catalog/cart/{request.user.get_shopping_cart().id}')

    else:
        form = PurchaseForm()
            
    return request.dmp.render('product.html', {
        'product': product,
        'form': form,
    })
    


###################################
### Product tile ajax endpoint


@view_function
def tile(request, product:cmod.Product):
    return request.dmp.render('product.tile.html', {
        'product': product,
    })


class PurchaseForm(forms.Form):
    quantity = forms.IntegerField(label='Quantity')

    def clean(self):
        qcart = 0
        SaleItem = None
        q = self.cleaned_data.get('quantity')
        mycart = self.sale
        SI = cmod.SaleItem.objects.filter(sale=self.sale)
        for item in SI:
                if self.product == item.product:
                    qcart = item.quantity

        if q is None or q == "0":
            raise forms.ValidationError('Quantity must be greater than zero.')
        if self.product.quantity < int(q) + qcart:
            raise forms.ValidationError('Insufficient inventory for this order')
    