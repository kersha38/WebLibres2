from django.db import models
from django.contrib.auth.models import User

class Facultad(models.Model):
    nombreF=models.CharField(max_length=30)

class Departamento(models.Model):
    nombreD = models.CharField(max_length=30)

class RegistroUsuario(models.Model):
    username=models.CharField(max_length=15)
    nombre=models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    cedula= models.CharField(max_length=13)
    email = models.EmailField()
    departamento = models.ForeignKey(Departamento,null=True,blank=True)
    facultad=models.ForeignKey(Facultad,null=True,blank=True)
    tipo=models.CharField(max_length=15,null=True,blank=True ,choices=(('e','estudiante'),('p','profesor')))
    user =models.ForeignKey(User,null=True,blank=True)

    def __str__(self):
        return self.username

    class Meta:
        permissions = (
            ("esEstudiante", "Puede Descargar"),
            ("esProfesor", "Puede Crear DEscargar Elminar y Modificar"),
        )
