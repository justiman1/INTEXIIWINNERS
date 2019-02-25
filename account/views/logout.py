from django.contrib.auth import authenticate, logout
from django.http import HttpResponseRedirect
from django_mako_plus import view_function
from django import forms
from django.conf import settings

@view_function
def process_request(request):
    logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect('/account/login')