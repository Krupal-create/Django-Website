# I have created this file - Krupal
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {'name': 'TechMachine ', 'place': 'INDIA'}
    return render(request, 'index.html',params)


def youtube(request):
    return HttpResponse("YOUTUBE <a href='/'>back</a>")
