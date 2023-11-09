
from django.urls import path
from control_post.views import lista_usuarios, crear_genero, lista_generos


urlpatterns = [

    path("usuarios/", lista_usuarios, name="lista_usuarios"),
    path("generos/", lista_generos, name="lista_generos"),
    path("crear-genero/", crear_genero, name="crear_genero"), 
]