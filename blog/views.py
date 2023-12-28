from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView
from .models import Post, Categoria
# Create your views here.

class IndexView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts_aprobados'
    def get_queryset(self):
        posts_aprobados = Post.objects.filter(estado = True)
        return posts_aprobados

class GeneralesView(ListView):
    model = Post
    template_name = 'generales.html'

class YacimientosView(ListView):
    model = Post
    template_name = 'yacimientos.html'
    context_object_name = 'posts_aprobados'
    def get_queryset(self):
        categoria_ = Categoria.objects.get(nombre='yacimientos')
        posts_yacimientos = Post.objects.filter(estado = True, categoria = categoria_)
        return posts_yacimientos
        


class PerforacionView(ListView):
    model = Post
    template_name = 'perforacion.html'
    context_object_name = 'posts_aprobados'
    def get_queryset(self):
        categoria_ = Categoria.objects.get(nombre='producción')
        posts_produccion = Post.objects.filter(estado = True, categoria = categoria_)
        return posts_produccion

