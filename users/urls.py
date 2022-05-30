from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from xml.dom.minidom import Document
from .views import home,form_Servicio,inicio, registro, barbero, modificar_servicio,delete
urlpatterns = [
    path('', home, name='admin-index' ),
    path('index',home,name='home'),
    path('iniciosesion/', inicio, name='iniciosesion'),
    path('registro/', registro, name='registro'),
    path('barbero/', barbero, name='barbero'),       
    path('form_Servicio/',form_Servicio,name='form_servicio'),
    path('modificar-servicio/<id>',modificar_servicio,name='modificar_servicio'),
    path('delete/<id>', delete,name='delete'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)