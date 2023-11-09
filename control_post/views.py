from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from control_post.models import usuario, genero, blogpost
from control_post.forms import GenFormu, UserFormu, PostFormu


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

def crear_usuario(request):
    if request.method == "POST":
        formulario = UserFormu(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            logname = data["logname"]
            contra = data["contra"]
            nombre = data["nombre"]
            apellido = data["apellido"]
            dni = data["dni"]
            email = data["email"]

            user = usuario(logname = logname, contra = contra, nombre = nombre, apellido = apellido, dni = dni, email = email)

            user.save()

            url_exitosa = reverse("lista_usuarios")
            return redirect(url_exitosa)
    else:
        formulario = UserFormu()
    http_response = render(

        request=request,
        template_name= "control_post/crear_usuario.html",
        context={"formulario": formulario}
    )
    return http_response



def buscar_usuarios(request):
    if request.method =="POST":
        data = request.POST
        busqueda = data["busqueda"]

        usuarios = usuario.objects.filter(nombre__contains=busqueda)

        contexto = {
            "usuarios": usuarios,
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

def buscar_generos(request):
    if request.method =="POST":
        data = request.POST
        busqueda = data["busqueda"]

        generos = genero.objects.filter(nombre__contains=busqueda)

        contexto = {
            "generos": generos,
        }
        http_response = render(
            request=request,
            template_name= "control_post/lista_generos.html",
            context=contexto,
        )
        return http_response



def lista_posteos(request):
    contexto = {

        "posteos": blogpost.objects.all()
    }

    http_response = render(

        request=request,
        template_name= "control_post/lista_posteos.html", 
        context=contexto,
    )
    return http_response


def crear_posteo(request):
    if request.method == "POST":
        formulario = PostFormu(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            autor = data["autor"]
            gen = data["gen"]
            fecha = data["fecha"]
            titulo = data["titulo"]
            content = data["content"]

            post = blogpost(autor = autor, gen = gen, fecha= fecha, titulo= titulo, content= content)

            post.save()

            url_exitosa = reverse("lista_posteos")
            return redirect(url_exitosa)
    else:
        formulario = PostFormu()
    http_response = render(

        request=request,
        template_name= "control_post/crear_posteo.html",
        context={"formulario": formulario}
    )
    return http_response


def buscar_posteo(request):
    if request.method =="POST":
        data = request.POST
        busqueda = data["busqueda"]

        posteos = blogpost.objects.filter(autor__contains=busqueda)

        contexto = {
            "posteos": posteos,
        }
        http_response = render(
            request=request,
            template_name= "control_post/lista_posteos.html",
            context=contexto,
        )
        return http_response