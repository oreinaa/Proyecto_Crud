from django.contrib import admin
from .models import Cliente, Producto, Factura, DetalleFactura
# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    #readonly_fields = ['creacion', 'modificacion']
    list_display= ('descripcion', 'precio', 'stock', 'iva')
    ordering  = ('descripcion',)
    search_fields= ('descripcion','precio')
    list_filter = ('descripcion',)

class ClienteAdmin(admin.ModelAdmin):
    
    list_display= ('ruc', 'nombre', 'direccion','get_producto')
    ordering  = ('nombre',)
    search_fields= ('nombre', 'ruc')
    list_filter = ('nombre',)

    def get_producto(self, obj):
        return "\n".join([p.descripcion for p in obj.producto.all()])

class FacturaAdmin(admin.ModelAdmin):
    readonly_fields = ['creacion', 'modificacion']
    list_display= ('cliente', 'total','creacion', 'modificacion')
    ordering  = ('cliente',)
    search_fields= ('cliente','total')
    list_filter = ('cliente',)

class DFacturaAdmin(admin.ModelAdmin):
   
    list_display= ('producto', 'cantidad','precio','subtotal')
    ordering  = ('producto',)
    search_fields= ('producto','cantidad')
    list_filter = ('producto',)


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Factura, FacturaAdmin)
admin.site.register(DetalleFactura, DFacturaAdmin)