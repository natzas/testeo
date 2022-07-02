from django.http import HttpResponse
from django.shortcuts import render
from Informacion.models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from Informacion.forms import *
from django.template import loader

# Create your views here.

#INICIO
def inicio(request):
    return render (request, "padre.html")

#ABOUT
def about(request):
    return render (request, "hijo_about.html")

#INICIAR SESION
def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request , data= request.POST)

        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario , password=contra)

            if user is not None:
                login(request, user)
                return render( request , "hijo_inicio.html" , {"mensaje":f"Bienvenido {usuario}"})
    
            else:
                return HttpResponse(f"Usuario Incorrecto")
        else:         
            return HttpResponse(f"FORM INCORRECTO {form}")

    form = AuthenticationForm()

    return render( request , "hijo_login.html" , {"form":form})

#REGISTRARSE X 1ERA VEZ
def register (request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse ( "Usuario creado")

    else:
        form = UserCreationForm()
        return render (request, "hijo_registro.html" , {"form":form})

#SUBIR ARCHIVOS
def upload(request):

    if request.method == "POST":

        mi_formulario = Upload( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data          
            
            profesional = Profesional( nombre=datos['nombre'] , apellido=datos['apellido'], profesion=datos['profesion'])
            profesional.save()

            return render( request , "hijo_form.html")

    return render( request, "hijo_form.html")
    
#BUSCAR ARCHIVOS
def buscar_profesional(request):

    return render( request , "hijo_buscar.html")

#MOSTRAR LA BUSQUEDA
def buscar(request):

    if request.GET['apellido']:
        apellido = request.GET['apellido']      
        profesional = Profesional.objects.filter(apellido__icontains = apellido)
        return render( request , "hijo_resultado_busqueda.html" , {"profesional": profesional})
    else:
        return HttpResponse("Campo vacio")

#MOSTRAR BLOG
def blog(request):
    profesional = Profesional.objects.all()
    blog = Archivo.objects.all()
    dicc = {"profesional" : profesional, "blog" : blog}
    plantilla = loader.get_template("hijo_blog.html")
    documento = plantilla.render(dicc)
    return HttpResponse( documento )