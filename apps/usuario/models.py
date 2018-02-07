from django.db import models
from django.contrib.auth.models import User

class RegistroUsuario(models.Model):
    username=models.CharField(max_length=15)
    nombre=models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    cedula= models.CharField(max_length=13)
    email = models.EmailField()
    departamento = models.CharField(max_length=30,null=True,blank=True)
    facultad=models.CharField(max_length=30)
    user =models.ForeignKey(User,null=True,blank=True)

    def __str__(self):
        return self.username

    class Meta:
        permissions = (
            ("esEstudiante", "Puede Descargar"),
            ("esProfesor", "Puede Crear DEscargar Elminar y Modificar"),
        )

