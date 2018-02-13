from django.contrib import admin
from apps.usuario.models import RegistroUsuario,Departamento,Facultad

# Register your models here.
admin.site.register(RegistroUsuario)
admin.site.register(Departamento)
admin.site.register(Facultad)