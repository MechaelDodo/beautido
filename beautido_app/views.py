from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

menu = ['Start', 'Photos', 'Hot girls', 'About']


def index(request):
    girls = Girls.objects.all()
    context = {
        'title': 'Start page',
        'menu': menu,
        'girls': girls
    }
    return render(request, 'beautido_app/index.html', context)


def about(request):
    context = {
        'title': 'About',
        'menu': menu
    }
    return render(request, 'beautido_app/about.html', context)


def index_second(request, secid):
    if request.GET:
        print(request.GET['name'])
    smth = "This is second page! %s " % secid
    return HttpResponse(smth)
