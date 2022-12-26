from django.http import HttpResponse
from django.shortcuts import render

def index (request):
    return render (request, "index.html", context={})

def saludo (request):
    return HttpResponse("Hola Mundo")

def Template (request):
    return render (request, "template1.html", context = {})