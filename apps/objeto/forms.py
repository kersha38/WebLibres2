from django import forms

from apps.objeto.models import objetoA,archivoCatalogador

class objetoAForm(forms.ModelForm):
    class Meta:
        model=objetoA

        fields=[
            'nombre',
            'descripcion',
            'autor',
            'institucion',
            'fechaCreacion',
            'fechaIngreso',
            'palabras_clave',
            'archivo',
            'tema'
        ]

        labels={'nombre':'nombre',
            'descripcion':'Descripcion',
            'autor':'Autor',
            'institucion':'Institucion',
            'fechaCreacion':'Fecha Creacion',
            'fechaIngreso':'Fecha Ingreso',
            'palabras_clave':'Palabras clave',
            'archivo':'Cargar Archivo',
            'tema':'Tema'

        }

        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'descripcion':forms.TextInput(attrs={'class':'form-control'}),
            'autor':forms.TextInput(attrs={'class':'form-control'}),
            'institucion':forms.TextInput(attrs={'class':'form-control'}),
            'fechaCreacion':forms.SelectDateWidget(),
            'fechaIngreso':forms.SelectDateWidget(),
            'palabras_clave':forms.TextInput(attrs={'class':'form-control'}),
            'archivo':forms.FileInput(attrs={'class':'form-control'}),
            'tema':forms.Select(attrs={'class':'form-control'})
        }

class archCatForm(forms.ModelForm):
    class Meta:
        model=archivoCatalogador
        fields=['archIndex',
                'archElp']
        labels={'archIndex':'Archivo index.html',
                'archElp':'Archivo .elp(exelearning)'}

        widgets={'archIndex':forms.FileInput(attrs={'class':'form-control'}),
                'archElp':forms.FileInput(attrs={'class':'form-control'})}