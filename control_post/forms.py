from django import forms


class GenFormu(forms.Form):
    nombre = forms.CharField (required=True, max_length=64)
    cantidad = forms.IntegerField()