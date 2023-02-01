# aqui van los enlaces de la aplicacion
from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_principal, name='pagina_principal'),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('home/', views.home, name='home'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
]
