from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def home(request):
    context = {
        title :"HOME"
    }
    return render(request, 'home.html' ,home)
