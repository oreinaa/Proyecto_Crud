from django.db import models
from django.utils import timezone
# Create your models here.
class Producto(models.Model):
    descripcion = models.CharField(max_length=100)
    precio = models.FloatField(default=0)
    stock = models.FloatField(default=0)
    iva = models.BooleanField(default=True)

    class Meta:
        verbose_name= 'Producto'
        verbose_name_plural= 'Productos'
        ordering= ['descripcion']
    
    def __str__(self):    
        return self.descripcion
    
#p1 = Producto(descripcion='Aceite Girasol', precio='1.50',stock='50')
#p1.save()

class Cliente(models.Model):
    ruc = models.CharField(max_length=13)
    nombre = models.CharField(max_length=300)
    direccion = models.TextField(blank=True, null=True)
    producto = models.ManyToManyField(Producto)

    class Meta:
        verbose_name= 'Cliente'
        verbose_name_plural= 'Clientes'
        ordering= ['nombre']
    
    def __str__(self):    
        return '{}'.format(self.nombre)
   

class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    creacion = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha Creacion")
    modificacion = models.DateTimeField(
        auto_now=True, verbose_name="Fecha Modificacion")
    total = models.FloatField(default=0)

    class Meta:
        verbose_name= 'Factura'
        verbose_name_plural= 'Factura'
        ordering= ['cliente']
    
    def __unicode__(self):
        return u'%s '%(self.cliente)
   
class DetalleFactura(models.Model):
    factura=models.ForeignKey(Factura, on_delete= models.CASCADE)
    producto=models.ForeignKey(Producto, on_delete= models.CASCADE)
    cantidad = models.FloatField(default=0)
    precio = models.FloatField(default=0)
    subtotal = models.FloatField(default=0)

    class Meta:
        verbose_name= 'DetalleFactura'
        verbose_name_plural= 'DetalleFacturas'
        ordering= ['producto']
    
    def __unicode__(self):
        return "{} ".format(self.factura)