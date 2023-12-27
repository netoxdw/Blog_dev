from django.contrib import admin
from .models import Categoria, Autor
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# user: userblog
# password: nosewe93

# Register your models here.
class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria


class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre', 'estado', 'fecha_creacion')
    resource_class = CategoriaResource


class AutorResource(resources.ModelResource):
    class Meta: 
        model = Autor


class AutorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombres', 'apellidos', 'email']
    list_display = ('nombres', 'apellidos', 'email')
    resource_class = AutorResource

admin.site.register(Autor, AutorAdmin)
admin.site.register(Categoria, CategoriaAdmin)
