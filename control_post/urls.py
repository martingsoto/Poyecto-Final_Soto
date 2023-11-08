
from django.urls import path
from control_post.views import lista_usuarios


urlpatterns = [

    path("usuarios/", lista_usuarios), 
]