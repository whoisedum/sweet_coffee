from django.contrib import admin
from django.urls import path, include
from coffee import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('coffee.urls')),  # Ruta principal conectada a coffee
    path('newsletter/', views.newsletter_view, name='newsletter'),
]
