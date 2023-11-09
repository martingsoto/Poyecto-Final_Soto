from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from control_post.models import usuario, genero
from control_post.forms import GenFormu


def lista_usuarios(request):
    contexto = {

        "usuarios": usuario.objects.all()
    }

    http_response = render(

        request=request,
        template_name= "control_post/lista_usuarios.html", 
        context=contexto,
    )
    return http_response


def lista_generos(request):
    contexto = {

        "generos": genero.objects.all()
    }

    http_response = render(

        request=request,
        template_name= "control_post/lista_generos.html", 
        context=contexto,
    )
    return http_response    


def crear_genero(request):
    if request.method == "POST":
        formulario = GenFormu(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data["nombre"]
            cantidad = 0

            gen = genero(nombre = nombre, cantidad = cantidad)

            gen.save()

            url_exitosa = reverse("lista_generos")
            return redirect(url_exitosa)
    else:
        formulario = GenFormu()
    http_response = render(

        request=request,
        template_name= "control_post/crear_genero.html",
        context={"formulario": formulario}
    )
    return http_response


