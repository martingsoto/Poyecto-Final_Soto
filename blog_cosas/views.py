from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse



def inicio_html(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='main.html',
        context=contexto,
    )
    return http_response


def about_html(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='about.html',
        context=contexto,
    )
    return http_response