
from django.urls import path

from inicio.views import bienvenida, fecha_y_hora, saludo, mi_template, mi_template2, mi_template3, condicionales_y_bucles , crear_auto


urlpatterns = [
    path('', bienvenida),
    path('fecha-y-hora/', fecha_y_hora),
    path('saludo/<str:nombre>/<str:apellido>/', saludo),
    path('mi-template/', mi_template),
    path('mi-template2/', mi_template2),
    path('mi-template3/', mi_template3),
    path('condicionales-y-bucles/', condicionales_y_bucles),
    path('crear-auto/<str:marca>/<str:modelo>/<int:anio>', crear_auto)
    
]