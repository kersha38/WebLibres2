from django.db import models

# Create your models here.
from django.db import models
class tema(models.Model):
    Nombre_tema=models.CharField(max_length=30)
    def __str__(self):
        return self.Nombre_tema

class objetoA(models.Model):
    nombre=models.CharField(max_length=40)
    descripcion=models.CharField(max_length=100,blank=True,null=True)
    autor=models.CharField(max_length=30)
    institucion=models.CharField(max_length=15,blank=True,null=True)
    fechaCreacion=models.DateField(default="2018-01-30")
    fechaIngreso=models.DateField()
    palabras_clave=models.CharField(max_length=30, null=True, blank=True)
    archivo=models.FileField(null=True, blank=True )
    tema=models.ForeignKey(tema,null=True,blank=True,on_delete=None)

    def __str__(self):
        return self.nombre

class archivoCatalogador(models.Model):
    # archivo de index es catalogado
    archIndex=models.FileField(upload_to='archCat')

    #archivo con el objeto exelearning
    archElp=models.FileField()