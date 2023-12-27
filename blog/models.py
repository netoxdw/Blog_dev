from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField('Nombre de la Categoría', max_length = 100, null = True, blank = False)
    estado = models.BooleanField('Activada/No activada', default = True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre
    
class Autor(models.Model):
    nombres = models.CharField('Nombres de autor', max_length = 250, null = False, blank = False)
    apellidos = models.CharField('Apellidos de autor', max_length = 250, null = False, blank = False)
    linkedin = models.URLField('LinkedIn', null = True, blank = True)
    facebook = models.URLField('Facebook', null = True, blank = True)
    instagram = models.URLField('Instagram', null = True, blank = True)
    twitter = models.URLField('x', null = True, blank = True)
    email = models.EmailField('Email', null = False, blank = False)
    estado = models.BooleanField('Activo/Desactivado', default = True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
    
    def __str__(self):
        return self.nombres


class Post(models.Model):
    titulo = models.CharField('Titulo', max_length = 90, null = False, blank = False)
    slug = models.CharField('Slug', max_length = 100, null = False, blank = False)
    descripcion = models.CharField('Descripción', max_length = 110, null = False, blank = False)
    contenido = RichTextField('Contenido', null = False, blank = False)
    imagen = models.URLField('Imagen', null = False, blank = False)
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    estado = models.BooleanField('Publicado/No publicado', default = True)
    fecha_creacion = models.DateField('Feacha de creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo