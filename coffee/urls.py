from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacto/', views.contacto, name='contacto'), 
    path('producto/', views.producto, name='producto'), 
    path('servicio/', views.servicio, name='servicio'), 
]