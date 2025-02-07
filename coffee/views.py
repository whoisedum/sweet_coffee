from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import NewsletterSubscriber

def newsletter_view(request):
    success = False
    error = None

    if request.method == 'POST':
        email = request.POST.get('email')  # Obtén el correo desde el formulario
        if email:
            # Verificar si el correo ya está registrado
            if NewsletterSubscriber.objects.filter(email=email).exists():
                error = "Este correo ya está registrado."
            else:
                # Registrar el correo y enviar el email
                NewsletterSubscriber.objects.create(email=email)
                send_mail(
                    '¡Gracias por suscribirte!',  # Asunto
                    'Te has suscrito a nuestra newsletter.',  # Mensaje
                    'eduardoolmedo224@gmail.com',  # Remitente
                    [email],  # Destinatario
                    fail_silently=False,
                )
                success = True

    return render(request, 'newsletter.html', {'success': success, 'error': error})




def home(request):
    return render(request, 'coffee/home.html')

def contacto(request):
    return render(request, 'coffee/contacto.html')

def producto(request):
    return render(request, 'coffee/producto.html')

def servicio(request):
    return render(request, 'coffee/servicio.html')

