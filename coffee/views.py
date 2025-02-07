from django.shortcuts import render

def home(request):
    return render(request, 'coffee/home.html')

def contacto(request):
    return render(request, 'coffee/contacto.html')

def producto(request):
    return render(request, 'coffee/producto.html')

def servicio(request):
    return render(request, 'coffee/servicio.html')
