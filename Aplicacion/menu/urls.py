from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarPlato/', views.registrarPlato),
    path('edicionPlato/<codigo>', views.edicionPlato),
    path('editarPlato/', views.editarPlato),
    path('eliminacionPlato/<codigo>', views.eliminarPlato),
    path('contacto/', views.contacto, name='contacto'),
    path('contacto.html/', views.contacto),
]