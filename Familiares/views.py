from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from Familiares.models import Familiares

def Familiar (request):
    familiares = Familiares.objects.create (Nombres = "Ayelen Johanna", Apellido = "Mackern", Con_Vida = True, Hijos = 0 )
    print(familiares)
    return HttpResponse("Mi familia es:")

def lista (request):
    lista = Familiares.objects.all()
    print (lista)
    context = {
        "Familiares" : lista,
    }
    return render (request, "Familiares.html", context=context)

def Borrador (request, id_familiar):
    Familiares = Familiares.objects.get(pk=id_familiar)
    Familiares.delete()
    Familiares = Familiares.objects.all()
    return render (request, "Familiares.html", context = Familiares)
