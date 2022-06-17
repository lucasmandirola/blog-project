from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Post(models.Model):
    image = models.ImageField(verbose_name='imagen', upload_to = 'blog/')
    title = models.CharField(max_length=200, verbose_name='titulo')
    desc = models.TextField(verbose_name='descripcion')
    content = RichTextField(verbose_name='contenido')
    created = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='fecha de actualizacion')

    class Meta:
        verbose_name = 'publicacion'
        verbose_name_plural = 'publicaciones'
        ordering = ['-created']