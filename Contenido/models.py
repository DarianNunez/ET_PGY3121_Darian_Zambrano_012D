import datetime
from tabnanny import verbose
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import User



class Categoria(models.Model):
	tipoProducto = models.CharField(primary_key=True, max_length=3, verbose_name="tipoProducto")
	nombreTipo = models.CharField(max_length=50, verbose_name="nombreTipo")
	
	def __str__(self):
		return self.nombreTipo

class Plantita(models.Model):
	idProducto = models.CharField(primary_key=True, max_length=4, verbose_name="idProducto")
	tituloProducto = models.CharField(max_length=50, verbose_name="tituloProducto")
	precio = models.IntegerField(verbose_name="precio")
	descripcion = models.CharField(max_length=300, verbose_name="descripcion")
	imagen = models.ImageField(upload_to="imagenes",null=True, blank=True,verbose_name="Imagen")
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="categoriaProduct")

	def __str__(self):
		return self.tituloProducto

class Boleta(models.Model):
    id_boleta=models.AutoField(primary_key=True)
    total=models.BigIntegerField()
    fechaCompra=models.DateTimeField(blank=False, null=False, default = datetime.datetime.now)
    
    def __str__(self):
        return str(self.id_boleta)


##Eliminando la tabla inferior se pueden eliminar datos
class detalle_boleta(models.Model):
    id_boleta = models.ForeignKey('Boleta', blank=True, on_delete=models.CASCADE)
    id_detalle_boleta = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey('Plantita', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.BigIntegerField()

    def __str__(self):
        return str(self.id_detalle_boleta)