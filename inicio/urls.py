
from django.urls import path

from inicio.views import bienvenida, fecha_y_hora, saludo, mi_template, mi_template2, mi_template3, condicionales_y_bucles , crear_auto, inicio

app_name= 'inicio'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('bienvenida/', bienvenida, name='bienvenida'),
    path('fecha-y-hora/', fecha_y_hora, name='fecha-y-hora'),
    path('saludo/<str:nombre>/<str:apellido>/', saludo, name='saludo'),
    path('mi-template/', mi_template, name='mi-template'),
    path('mi-template2/', mi_template2, name='mi-template2'),
    path('mi-template3/', mi_template3, name='mi-template2'),
    path('condicionales-y-bucles/', condicionales_y_bucles, name='condicionales-y-bucles'),
    path('crear-auto/<str:marca>/<str:modelo>/<int:anio>', crear_auto, name='crear-auto')
    
]