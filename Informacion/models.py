from django.db import models

# Create your models here.
class Profesional(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    profesion = models.CharField(max_length=40)


class Archivo(models.Model):
    titulo= models.CharField(max_length=40) #str corto
    subtitulo = models.CharField(max_length=40) # str corto
    cuerpo = models.TextField()
    fecha = models.DateField()
    imagen = models.ImageField(null=True, blank=True, upload_to="images/")
    adjunto = models.FileField(null=True, blank=True, upload_to="images/")
    autor = Profesional.nombre
   

    def __str__(self):
        return self.titulo