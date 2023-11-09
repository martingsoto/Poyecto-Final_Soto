from django import forms



class GenFormu(forms.Form):
    nombre = forms.CharField (required=True, max_length=64)
    cantidad = forms.IntegerField()

class UserFormu(forms.Form):
    logname = forms.CharField(required=True,max_length=64)
    contra = forms.CharField(required=True, max_length=12)
    nombre = forms.CharField(required=True, max_length=64)
    apellido = forms.CharField(required=True, max_length=64)
    dni = forms.IntegerField(required=True)
    email = forms.EmailField()
    

class PostFormu(forms.Form):
    autor = forms.CharField(required=True, max_length=64)
    gen = forms.CharField(required=True, max_length=64)
    fecha = forms.DateField(required=True,)
    titulo = forms.CharField(max_length=126)
    content = forms.CharField(max_length=8000)

