
from django.urls import path
from control_post.views import (
    lista_usuarios,
    crear_usuario,
    buscar_usuarios,


    crear_genero, 
    lista_generos, 
    buscar_generos,

    crear_posteo, 
    lista_posteos, 
    buscar_posteo,
    
    
    
    )


urlpatterns = [

    path("usuarios/", lista_usuarios, name="lista_usuarios"),
    path("crear-usuario/", crear_usuario, name="crear_usuario"),
    path("buscar-usuarios", buscar_usuarios, name="buscar_usuarios"),


    path("generos/", lista_generos, name="lista_generos"),
    path("crear-genero/", crear_genero, name="crear_genero"),
    path("buscar-generos", buscar_generos, name="buscar_generos"),


     path("posteos/", lista_posteos, name="lista_posteos"),
    path("crear-posteo/", crear_posteo, name="crear_posteo"),
    path("buscar-posteo", buscar_posteo, name="buscar_posteo"),  
]