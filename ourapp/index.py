from django.http import HttpResponse
from django.shortcuts import render

def webhome(request):
    return render(request, 'home.html')

def webabout(request):
    return render(request, 'about.html')

def webcontact(request):
    return render(request, 'contact.html')

def weblogin(request):
    return render(request, 'login.html')

def webregister(request):
    return render(request, 'register.html')

def webservice(request):
    return render(request, 'service.html')
