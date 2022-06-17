from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='titulo')
    desc = models.TextField(verbose_name='descripcion')
    created = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='fecha de actualizacion')

    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['-created']