from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate

from perfiles.forms import UserRegisterForm, UserUpdateForm


def registro(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            url_exitosa = reverse("inicio")
            return redirect(url_exitosa)
    else:
        formulario = UserRegisterForm()
    return render(

        request = request,
        template_name = "perfiles/registro.html",
        context={"form": formulario},
    )



def login_view(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(request, data= request.POST)

        if form.is_valid():
            data = form.cleaned_data
            usuario = data.get('username')
            password = data.get('password')
            user = authenticate(username=usuario, password=password)
            if user:
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)
                url_exitosa = reverse('inicio')
                return redirect(url_exitosa)
    else:
        form = AuthenticationForm()
    return render(

        request= request,
        template_name= "perfiles/login.html",
        context={'form': form},
    )


class CustomLogoutView(LogoutView):
    template_name = "perfiles/logout.html"


class MiPerfilUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserUpdateForm
    succes_url = reverse_lazy ('inicio')
    template_name = 'perfiles/formulario_perfil.html'

    def get_object(self, queryset=None):
        return self.request.user


def ver_perfil(request, id):
    usuario = User.objects.get(id=id)

    data = {
            
            "first_name" : usuario.first_name,
            "last_name" : usuario.last_name,
            'username' : usuario.username,
            'email' : usuario.email,
        }
    http_response = render(

        request=request,
        template_name= "perfiles/ver_perfil.html", 
        context={"perfil": data },
    )
    return http_response

# Create your views here.
