from django.db import models
class Facultad(models.Model):
    nombre_Facultad=models.CharField(max_length=30)
    def __str__(self):
        return self.nombre_Facultad


class Departamento(models.Model):
    nombre_Dept=models.CharField(max_length=30)
    def __str__(self):
        return self.nombre_Dept

# Create your models here.
class usuario(models.Model):
    nick=models.CharField(max_length=15)
    clave=models.CharField(max_length=15)
    correo=models.EmailField()
    cedula=models.CharField(max_length=13)
    nombre=models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    #departamento=models.CharField(max_length=15)
    #facultad=models.CharField(max_length=15)
    departamento=models.ForeignKey(Departamento,null=True,blank=True,on_delete=None)
    facultad= models.ForeignKey(Facultad, null=True, blank=True, on_delete=None)
    def __str__(self):
        return self.nick

class PermisoUsuario(models.Model):
    usuario=models.OneToOneField(usuario)
    tipo=models.CharField(max_length=10,choices=(('e','estudiante'),('p','profesor')))

    def __str__(self):
        return self.tipo


class tema(models.Model):
    Nombre_tema=models.CharField(max_length=15)
    def __str__(self):
        return self.Nombre_tema

class objetoA(models.Model):
    nombre=models.CharField(max_length=15)
    descripcion=models.CharField(max_length=50)
    autor=models.CharField(max_length=30)
    institucion=models.CharField(max_length=15)
    fechaCreacion=models.DateField(default="2018-01-30")
    fechaIngreso=models.DateField()
    palabras_clave=models.CharField(max_length=30, null=True)
    archivo=models.FileField(null=True, blank=True )
    tema=models.ForeignKey(tema,null=True,blank=True,on_delete=None)

    def __str__(self):
        return self.nombre

