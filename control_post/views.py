from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from control_post.models import blogpost
from control_post.forms import  PostFormu


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


def ver_posteo(request, id):
    
    
    posteo = blogpost.objects.get(id=id)

    data = {
            
            "gen" : posteo.gen,
            "fecha" : posteo.fecha,
            'titulo' : posteo.titulo,
            'content' : posteo.content,
        }

    http_response = render(

        request=request,
        template_name= "control_post/ver_posteo.html", 
        context={"articulo": data },
    )
    return http_response


@login_required
def crear_posteo(request):
    if request.method == "POST":
        formulario = PostFormu(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            
            gen = data["gen"]
            fecha = data["fecha"]
            titulo = data["titulo"]
            content = data["content"]

            post = blogpost( gen = gen, fecha= fecha, titulo= titulo, content= content, creador= request.user)

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


@login_required
def editar_posteo(request, id):
    posteo = blogpost.objects.get(id=id)
    if request.method == "POST":
        formulario = PostFormu(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
           
           
            posteo.gen = data["gen"]
            posteo.fecha = data["fecha"]
            posteo.titulo = data["titulo"]
            posteo.content = data["content"]

            posteo.save()

            url_exitosa = reverse("lista_posteos")
            return redirect(url_exitosa)
    else:
        inicial = {
            
            "gen" : posteo.gen,
            "fecha" : posteo.fecha,
            'titulo' : posteo.titulo,
            'content' : posteo.content,
        }
        formulario = PostFormu(initial=inicial)
    return render(
        request=request,
        template_name= 'control_post/crear_posteo.html',
        context={"formulario": formulario},
    ) 
    

@login_required
def eliminar_posteo(request, id):
    posteo = blogpost.objects.get(id=id)

    if request.method == "POST":
        posteo.delete()

        url_exitosa = reverse("lista_posteos")

        return redirect(url_exitosa)


