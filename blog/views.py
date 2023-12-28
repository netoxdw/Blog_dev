from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class GeneralesView(TemplateView):
    template_name = 'generales.html'

class YacimientosView(TemplateView):
    template_name = 'yacimientos.html'

class PerforacionView(TemplateView):
    template_name = 'perforacion.html'
