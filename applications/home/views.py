from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class inicio(TemplateView):
    template_name = 'inicio.html'