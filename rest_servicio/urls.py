from django.urls import path
from rest_servicio.views import detalle_servicio, lista_servicios
from rest_servicio.viewsLogin import login

urlpatterns = [
    path('lista_servicios',lista_servicios, name="lista_servicios"),
    path('detalle_servicio/<id>',detalle_servicio,name='detalle_servicio'),
    path('login',login,name='login'),
]