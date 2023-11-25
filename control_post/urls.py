
from django.urls import path
from control_post.views import (


    crear_posteo, 
    lista_posteos, 
    
    editar_posteo,
    eliminar_posteo,
    ver_posteo,

    
    
    
    )


urlpatterns = [

    path("posteos/", lista_posteos, name="lista_posteos"),
    path("crear-posteo/", crear_posteo, name="crear_posteo"),
    path("pages/page<int:id>/", ver_posteo, name="ver_posteo"),
    path("editar-posteo/<int:id>/", editar_posteo, name="editar_posteo"),
    path("eliminar-posteo/<int:id>/", eliminar_posteo, name="eliminar_posteo"),  
]