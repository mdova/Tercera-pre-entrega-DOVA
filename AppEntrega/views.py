from django.shortcuts import render, redirect
from django.template import loader
from .forms import *
from .models import *
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, 'AppEntrega/inicio.html')

def padre(request):
    return  render(request, 'AppEntrega\inicio_padre.html')

def construccion(request):
    return render(request, r'AppEntrega\under_construction.html')

def proveedores(request):
    if request.method == 'POST':
        form_proveedores = ProveedoresFormulario(request.POST)
        if form_proveedores.is_valid():
            datos = form_proveedores.cleaned_data
            proveedor = Proveedores(empresa=datos['empresa'], cuit=datos['cuit'], localidad=datos['localidad'])
            proveedor.save()
            return redirect('pagina principal')
    else:
     form_proveedores = ProveedoresFormulario()
    return render(request, r'AppEntrega/proveedores.html', {'formulario_proveedores':form_proveedores})


def respuesta_proveedores(request):
    if request.method == 'GET':
       empresa = request.GET['empresa']
       proveedor = Proveedores.objects.filter(empresa__icontains=empresa)
       return render(request, r'AppEntrega/resultados-proveedores.html', {'empresa':empresa,'proveedor':proveedor} )
    else:
       respuesta = 'Proveedor no encontrado'
    return HttpResponse(respuesta)
       
def respuesta_vendedores(request):
    if request.method == 'GET':
       nombre = request.GET['nombre']
       vendedor = Vendedores.objects.filter(nombre__icontains=nombre)
       return render(request, r'AppEntrega/resultados-vendedores.html', {'nombre':nombre,'vendedor':vendedor} )
    else:
       respuesta = 'Vendedor no encontrado'
    return HttpResponse(respuesta)

def respuesta_productos(request):
    if request.method == 'GET':
       sku = request.GET['SKU']
       producto = Productos.objects.filter(sku__icontains=sku)
       return render(request, r'AppEntrega/resultados-productos.html', {'SKU':sku,'producto':producto} )
    else:
       respuesta = 'Producto no encontrado'
    return HttpResponse(respuesta)


def productos(request):
    if request.method == 'POST':
        form_productos = ProductosFormulario(request.POST)
        if form_productos.is_valid():
            datos = form_productos.cleaned_data
            producto = Productos(sku=datos['sku'], descripcion=datos['descripcion'], fecha_de_carga=datos['fecha'], disponibilidad=datos['disponibilidad'])
            producto.save()
            return redirect('pagina principal')
    else:
     form_productos = ProductosFormulario()
    return render(request, r'AppEntrega/productos.html', {'formulario_productos':form_productos})

def vendedores(request):
    if request.method == 'POST':
        form_vendedores = VendedoresFormulario(request.POST)
        if form_vendedores.is_valid():
            datos = form_vendedores.cleaned_data
            vendedor = Vendedores(nombre=datos['nombre'], dni=datos['dni'], activo_actualmente=datos['activo_actualmente'])
            vendedor.save()
            return redirect('pagina principal')
    else:
     form_vendedores = VendedoresFormulario()
    return render(request, r'AppEntrega/vendedores.html', {'formulario_vendedores':form_vendedores})