
from django.contrib import admin
from django.urls import path, include

from . import index

urlpatterns = [
    #path('admin/', admin.site.urls),
    
    path('', index.webhome, name='webhome'),
    path('service', index.webservice, name='webservice'),
    path('contact', index.webcontact, name='webcontact'),
    path('login', index.weblogin, name='weblogin'),
    path('register', index.webregister, name='webregister'),
    path('about', index.webabout, name='webabout'),
    path('', include('app1.urls')),

    

]
