from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'barberos/index.html')

def inicio(request):
    return render(request,'barberos/iniciosesion.html')

def registro(request):
    return render(request,'barberos/registro.html')

def barbero(request):
    return render(request,'barberos/barberos.html')