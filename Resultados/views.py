from django.shortcuts import render
from django.views.generic import ListView

def inicio(request):
    return render(request,'Inicio.html')

from .models import estadisticas
class PersonListView(ListView):
    model = estadisticas
    template_name = 'Tabla.html'
