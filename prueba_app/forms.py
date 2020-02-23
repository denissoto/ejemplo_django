from django import forms
from prueba_app import models

class clientes(forms.ModelForm):
    class Meta:
        model= models.clientes
        fields= ('nombre','apellido','documento')
        labels= {'nombre':'Nombre','apellido':'Apellido','documento':'Carné de identidad'}
        widgets= {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'apellido':forms.TextInput(attrs={'class':'form-control'}),
            'documento':forms.TextInput(attrs={'class':'form-control'}),
        }

class productos(forms.ModelForm):
    class Meta:
        model= models.productos
        fields= ('codigo','descripcion','precio')
        labels= {'codigo':'Código de producto','descripcion':'Descripción','precio':'Precio'}
        widgets= {
            'codigo':forms.TextInput(attrs={'class':'form-control'}),
            'descripcion':forms.TextInput(attrs={'class':'form-control'}),
            'precio':forms.TextInput(attrs={'class':'form-control'}),
        }