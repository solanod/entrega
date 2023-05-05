from django.shortcuts import render, redirect
from facturas.models import Detalle_Factura
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Utilities
from datetime import datetime


@login_required
def factura(request):
    """"Return a greeting. """
    now = datetime.now().strftime('%m/%d/%Y, %H:%M:%S')
    now2 = datetime.now()
    productos = Detalle_Factura.objects.all()        
    return render(request, "facturas/facturas.html", {'now2': now2})
