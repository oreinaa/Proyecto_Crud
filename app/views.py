from django.shortcuts import render, redirect

from django.http import HttpResponse
from .forms import ClienteForm, ProductoForm, FacturaForm, DetalleFForm
from .models import Producto, Cliente, Factura, DetalleFactura

def menu(request):  #Ese parametro siempre va
    opc = {'Menu': 'Menu Principal','Producto': 'Productos', 'Cliente':   #Diccionario
          'Clientes','Factura':'Facturas','DetalleF':'Detalle de Factura', 'Venta':'Ventas'}
    return render(request, 'principal.html', opc)

def producto(request):
     opc = {'Menu': 'Menu Principal', 'Producto': 'Productos', 'Cliente':   
          'Clientes','Factura':'Facturas','DetalleF':'Detalle de Factura','Venta': 'Ventas', 'accion': 'Guardar'}
      
     if request.method == 'POST':
            form = ProductoForm(request.POST)
            if form.is_valid():    #Valida que esten los datos
                  form.save()      
                  return redirect('listarproducto')
     else:
            form = ProductoForm()
            opc ['form']= form

     return render(request, 'producto.html', opc)

def  editarProducto (request,id ):
    opc  = { 'Menú' : 'Menú principal' ,
                'Producto' : 'Productos' , 'Cliente' : 'Clientes','Factura':'Facturas','DetalleF':'Detalle de Factura' ,'Venta': 'Ventas', 'accion' : 'Actualizar' }
    producto = Producto.objects.get(id=id)
    if request.method == 'GET':
        form = ProductoForm(instance=producto)
        opc['form'] = form
    else:
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listarproducto')

    return render(request, 'producto.html', opc)

def listarProducto(request):
    producto = Producto.objects.all()
    opc = {'Menu': 'Menu Principal',
                'Producto': 'Productos', 'Cliente': 'Clientes','Factura':'Facturas','DetalleF':'Detalle de Factura','Venta': 'Ventas', 'productos': producto}
    return render(request, 'listar_producto.html', opc)

def eliminarProducto(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('listarproducto')
    return render(request, 'eliminar_producto.html', {'Producto': producto})


def cliente(request):
      opc = {'Menu': 'Menu Principal', 'Producto': 'Productos', 'Cliente':   
          'Clientes','Factura':'Facturas','DetalleF':'Detalle de Factura','Venta': 'Ventas', 'accion': 'Guardar'}

      if request.method == 'POST':
            form = ClienteForm(request.POST)
            if form.is_valid():    #Valida que esten los datos
                  form.save()
                  return redirect('listarcliente')
      else:
            form = ClienteForm()
            opc ['form']= form
      return render(request, 'cliente.html', opc)

def  editarCliente (request,id ):
    opc  = { 'Menú' : 'Menú principal' ,
                'Producto' : 'Productos' , 'Cliente' : 'Clientes','Factura':'Facturas','DetalleF':'Detalle de Factura','Venta': 'Ventas' , 'accion' : 'Actualizar' }
    cliente = Cliente.objects.get(id=id)
    if request.method == 'GET':
        form = ClienteForm(instance=cliente)
        opc['form'] = form
    else:
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listarcliente')
    return render(request, 'cliente.html', opc)

 
def listarCliente(request):
    cliente = Cliente.objects.all()
    
    opc = {'Menu': 'Menu Principal',
                'Producto': 'Productos','Cliente': 'Clientes','Factura':'Facturas','DetalleF':'Detalle de Factura','Venta': 'Ventas', 'clientes': cliente}
    
    return render(request, 'listar_cliente.html', opc)


def eliminarCliente(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('listarcliente')
    return render(request, 'eliminar_cliente.html', {'Cliente': cliente})


def factura(request):
      opc = {'Menu': 'Menu Principal', 'producto': 'Productos', 'cliente':   
          'Clientes','Factura':'Facturas','DetalleF':'Detalle de Factura','Venta': 'Ventas', 'accion':'Guardar'}

      if request.method == 'POST':
            form = FacturaForm(request.POST)
            if form.is_valid():    #Valida que esten los datos
                  form.save()
                  return redirect('listarventas')
      else:
            form = FacturaForm()
            opc ['form']= form
      return render(request, 'principal.html', opc)

def listarVentas(request):
    factura = Factura.objects.all()
    
    opc = {'Menu': 'Menu Principal',
                'Producto': 'Productos','Cliente': 'Clientes','Factura':'Facturas','Venta': 'Ventas', 'facturas': factura}
    
    return render(request, 'listar_ventas.html', opc)

