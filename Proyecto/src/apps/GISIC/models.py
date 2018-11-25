from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Entrada(models.Model):
    
    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    contenido = models.TextField()
    slug = models.SlugField()
    
    def _unicode_(self):
        return self.titulo
        
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.titulo)
        super(Entrada,self).save(*args, **kwargs)