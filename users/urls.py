from django.urls import path
from .views import index, inicio, registro, barbero
urlpatterns = [
    path('', index, name='admin-index' ),
    path('iniciosesion/', inicio, name='iniciosesion'),
    path('registro/', registro, name='registro'),
    path('barbero/', barbero, name='barbero'),
]
