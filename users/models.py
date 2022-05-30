from django.db import models

# Create your models here.
class TipoServicio(models.Model):
    idTipoServicio = models.IntegerField(primary_key=True,verbose_name='Id')
    nombreTipoServicio = models.CharField(max_length=50,verbose_name='Tipo de Servicio')

    def __str__(self):
        return self.nombreTipoServicio
    
class Servicio(models.Model):
    idServicio = models.IntegerField(primary_key=True, verbose_name='Id Servicio')
    nombreServicio = models.CharField(max_length=50, verbose_name='Nombre Servicio')
    img = models.ImageField(upload_to = 'users/static/barb/img/', default='', verbose_name = 'Imagen Servicio')
    descripcionServicio = models.CharField(max_length=200,null=True, blank=True, verbose_name='Descripción Servicio')
    categoria = models.ForeignKey(TipoServicio, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreServicio