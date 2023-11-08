from django.shortcuts import render
from django.http import HttpResponse


def lista_usuarios(request):
    contexto = {}


    http_response = render(

        request=request,
        template_name= "control_post/lista_usuarios.html", 
        context=contexto,
    )
    return http_response