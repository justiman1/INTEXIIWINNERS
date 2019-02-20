from django.conf import settings
from django_mako_plus import view_function, jscontext
from account import models as amod
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
]


@view_function
def process_request(request):

   
    context = {
    }
    return request.dmp.render('login.html', context)


