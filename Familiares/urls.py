from django.urls import path

from Familiares.views import Familiar, lista, Borrador

urlpatterns = [
    path("familiar/", Familiar),
    path("lista/", lista),
    path("borrador/", Borrador),
]