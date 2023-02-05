from django.db import models

# Create your models here.
class maquillaje(models.Model):
    tipo = models.CharField('tipo', max_length=50, null=False)
    price = models.IntegerField()
    nombre = models.CharField('nombre', max_length=43)
    descripcion = models.CharField('descripcion', max_length=255)
    img = models.ImageField('imagen', blank=False, upload_to= 'media/')
    def __str__(self):
        return self.nombre+' '+str(self.price)+'$'