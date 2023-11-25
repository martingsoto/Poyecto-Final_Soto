from django.contrib import admin
from django.urls import path

from perfiles.views import registro, login_view, CustomLogoutView, MiPerfilUpdateView, ver_perfil



urlpatterns = [
    
    path("registro/", registro, name="registro"),
    path('login/', login_view, name="login"),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('editar-mi-perfil/', MiPerfilUpdateView.as_view(), name="editar_perfil"),
    path("perfil/perfil<int:id>/", ver_perfil, name="ver_perfil"),
  
    ]
