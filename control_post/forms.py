from django import forms


class PostFormu(forms.Form):
    
    gen = forms.CharField(required=True, max_length=64)
    fecha = forms.DateField(required=True,)
    titulo = forms.CharField(max_length=126)
    content = forms.CharField(max_length=8000)

