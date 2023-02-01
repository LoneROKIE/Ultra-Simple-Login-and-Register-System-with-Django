# imports :
from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# nos lleva a la pagina principal
def pagina_principal(request): 
    return render(request, 'pagina_principal.html')

@login_required
def home(request):
    return render(request, 'home.html')

# vista para crear un usuario
def crear_usuario(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        usuario = Usuario.objects.create_user(username=username,email=email, password=password)
        usuario.save()
        return render(request, 'pagina_principal.html')
    return render(request, 'crear_usuario.html')

# vista para iniciar sesion
def iniciar_sesion(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        usuario = authenticate(request, username=username,email=email, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('home')
        else:
            return render(request, 'iniciar_sesion.html')
    else:
        return render(request, 'iniciar_sesion.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('pagina_principal')
