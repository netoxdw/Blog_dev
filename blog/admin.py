from django.contrib import admin
from .models import Categoria, Autor
# user: userblog
# password: nosewe93

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre', 'estado', 'fecha_creacion')
admin.site.register(Categoria, CategoriaAdmin)

class AutorAdmin(admin.ModelAdmin):
    search_fields = ['nombres', 'apellidos', 'email']
    list_display = ('nombres', 'apellidos', 'email')

admin.site.register(Autor, AutorAdmin)
