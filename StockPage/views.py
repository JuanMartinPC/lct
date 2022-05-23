from django.shortcuts import render, redirect
from StockPage.models import Productos
from .forms import ProductosForm

def inicio(request):
    return render(request,'inicio.html')
    
def productos(request):
    productos= Productos.objects.all()
    cantidad_total = int(len(productos))

    en_stock = Productos.objects.exclude(stock=0)
    en_stock = len(en_stock)

    sin_stock = Productos.objects.filter(stock=0)
    sin_stock = len(sin_stock)

#  for i in productos:
 #       if productos.stock == 0:
  #          sin_stock=+1
   #     else:
    #        en_stock=+1"""
    
        
    context= {'productos':productos, 'cantidad_total': cantidad_total, 'en_stock':en_stock, 'sin_stock': sin_stock}
    return render(request, 'productos.html', context)

def crear(request):
    formulario = ProductosForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('productos')
    return render(request, 'crear.html', {'formulario':formulario})

def editar(request, id):
    producto = Productos.objects.get(id=id)
    formulario = ProductosForm(request.POST or None, request.FILES or None, instance=producto)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('productos')
    return render(request, 'editar.html', {'formulario':formulario})

def eliminar(request, id):
    producto = Productos.objects.get(id=id)
    producto.delete()
    return redirect('productos')

