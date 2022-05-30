from ast import Return
from django.shortcuts import render,redirect
from users.models import Servicio
from .forms import ServicioForm

# Create your views here.
def index(request):
    return render(request, 'barberos/index.html')

def inicio(request):
    return render(request,'barberos/iniciosesion.html')

def registro(request):
    return render(request,'barberos/registro.html')

def barbero(request):
    return render(request,'barberos/barberos.html')

def home(request):
    servicios = Servicio.objects.all()
    datos = {
        'servicios':servicios
    }
    return render(request, 'barberos/index.html',datos)

def form_Servicio(request):
    form= ServicioForm()
    return render(request, 'barberos/formulario.html',{'form':form})

def form_Servicio(request):
    datos = {
        'form': ServicioForm()
    }

    if request.method == 'POST':
        formulario = ServicioForm(request.POST or None, request.FILES or None) #Carga de archivos        
        if formulario.is_valid():
            formulario.save() #inserta la BD
            datos['mensaje'] = 'Se guardó Producto'
        else:
            datos['mensaje'] = 'NO se guardó Producto'
    
    return render(request, "barberos/formulario.html",datos)

def modificar_servicio(request, id):
    servicio = Servicio.objects.get(idServicio = id)

    datos = {
        'form':ServicioForm(instance=servicio)
    }
    if(request.method == 'POST'):
        servicio = ServicioForm(data=request.POST, instance=servicio)
        if servicio.is_valid():
            servicio.save()
            datos['mensaje'] = 'Modificado Correctamente'
        else:           
            datos['mensaje'] = 'NO se modificó producto'


    return render(request, 'barberos/modificar-servicio.html', datos)

def delete(request, id):
    servicio = Servicio.objects.get(idServicio = id)
    servicio.delete()

    return redirect(to='home')