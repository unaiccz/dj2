from django.shortcuts import render
from django.views.generic import ListView

from applications.maquillajes.models import maquillaje
# Create your views here.
class maquillajes(ListView):
    model = maquillaje
    context_object_name = 'mk'
    template_name = 'maquillaje/listado.html'
class search(ListView):
    model = maquillaje
    template_name = 'maquillaje/searchto.html'

    def get_queryset(self):
        clave = self.request.GET.get('search','')
        lista = maquillaje.objects.filter(

            tipo__icontains = clave
        )
        return lista
