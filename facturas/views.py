from django.shortcuts import render, redirect
from facturas.models import Detalle_Factura
<<<<<<< HEAD
from django.contrib.auth.decorators import login_required
from productos.carrito import Carrito
from productos.models import Producto



# Utilities
from datetime import datetime

=======
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Utilities
from datetime import datetime


>>>>>>> 1259a63e81275d98bc1194d18c5dc498eb9c297b
@login_required
def factura(request):
    prostop = Producto.objects.all()
    carrito = Carrito(request)
    now = datetime.now().strftime('%m/%d/%Y, %H:%M:%S')
    now2 = datetime.now()
    productos = Detalle_Factura.objects.all()        
<<<<<<< HEAD
    return render(request, "facturas/facturas.html", {'prostop':prostop, 'carrito': carrito, 'now': now})

def guardar_carrito(request):
    carrito = Carrito(request)
    carrito.guardar_carrito()
    return redirect("Tienda")
=======
    return render(request, "facturas/facturas.html", {'now2': now2})
>>>>>>> 1259a63e81275d98bc1194d18c5dc498eb9c297b
