from django.contrib import admin
from .models import Categoria, Autor
# user: userblog
# password: nosewe93

# Register your models here.
# class CategoriaAdmin(admin.AdminSite):
admin.site.register(Categoria)
admin.site.register(Autor)
