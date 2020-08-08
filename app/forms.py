from django import forms
from .models import Cliente, Producto, Factura, DetalleFactura


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('descripcion', 'precio', 'stock', 'iva')
        label = {'descripcion': 'Descripcion', 'precio': 'Precio', 'stock': 'Stock', 'iva': 'IVA'}
        
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('ruc', 'nombre', 'direccion', 'producto')
        label = {'ruc': 'RUC', 'nombre': 'Nombre', 'direccion': 'Direccion', 'producto': 'Producto'}

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ('cliente', 'total')
        label = {'cliente': 'Cliente', 'total': 'Total'}

class DetalleFForm(forms.ModelForm):
    class Meta:
        model = DetalleFactura
        fields = ('factura', 'producto','precio','cantidad','subtotal')
        label = {'factura': 'Cliente', 'producto': 'Producto','precio':'Precio','cantidad':'Cantidad','subtotal':'Subtotal'}