from django import forms

class Upload(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    profesion = forms.CharField(max_length=40)
    titulo= forms.CharField(max_length=40) #str corto
    subtitulo = forms.CharField(max_length=40) # str corto
    cuerpo = forms.CharField()
    fecha = forms.DateField()