from apps.usuario.models import RegistroUsuario
from django import forms

class registroForm(forms.ModelForm):
    class Meta:
        model = RegistroUsuario

        fields = [
            'username',
            'nombre',
            'apellido',
            'cedula',
            'email',
            'departamento',
            'facultad',
            'tipo'
        ]

        labels = {'username':'Username',
            'nombre':'Nombre',
            'apellido':'Apellido',
            'cedula':'Cedula',
            'email':'Correo',
            'departamento':'Departamento',
            'facultad':'Facultad',
            'tipo':'Tipo de usuario'

                  }

        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'apellido':forms.TextInput(attrs={'class':'form-control'}),
            'cedula':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'departamento':forms.Select(),
            'facultad':forms.Select(),
            'tipo':forms.Select(choices=(('e','estudiante'),('p','profesor')))
        }

