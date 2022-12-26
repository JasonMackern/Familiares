from django.http import HttpResponse
from django.shortcuts import render

def saludo (request):
    return HttpResponse("Hola Mundo")

def Template (request):
    return render (request, "template1.html", context = {})