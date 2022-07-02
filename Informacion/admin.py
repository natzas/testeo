from django.contrib import admin
from .models import *


# Register your models here.
#para que desde el panel de administracion pda ver los modelos

admin.site.register(Profesional)
admin.site.register(Archivo)
