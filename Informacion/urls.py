from django.urls import path
#IMPORTAR LAS VIEWS
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.inicio, name="home"),
    path("about" , views.about , name="about" ),
    path("blog" , views.blog , name="blog" ),
    path("upload" , views.upload, name="upload"),
    path("login", views.login_request, name="login"),
    path("register", views.register, name="register"),
    path("logout", LogoutView.as_view (template_name= "hijo_logout.html"), name="logout"),
    path("buscar_profesional" , views.buscar_profesional),
    path("buscar" , views.buscar)
]