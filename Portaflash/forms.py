from django import forms
from django.forms.widgets import *
from django.forms.fields import ChoiceField
from Portaflash.models import *
from django.contrib.auth.models import User

EstadoMaquinaria=(
	('Activa','Activa'),
	('En Reparacion','En Reparacion'),
	('En Mantencion','En Mantencion'),
	('Desactivada','Desactivada'),
	)


####Ingresar Usuario
class UsuarioForm(forms.ModelForm):
	class Meta:
		model= Usuario #Tabla a referenciar
		fields= ['rutUsuario','nombreUsuario','apellidoUsuario'] #atributos a ingresar
		widgets={
				'rutUsuario': forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder':'Rut','style':'width:50%'}),
				'nombreUsuario': forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder':'Nombre','style':'width:50%'}),
				'apellidoUsuario': forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder':'Apellido','style':'width:50%'}),
			}


###BASE PARA LOS INGRESAR
class MaquinariaForm(forms.ModelForm):
	class Meta:
		model= PuestoTrabajo
		fields= ['puestoTrabajo','estadoMaquinaria']
		widgets={
			'puestoTrabajo': forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder':'Nombre','style':'width:50%'}),
			'estadoMaquinaria': forms.Select(attrs={'class':'form-control','placeholder':'Nombre','style':'width:50%'})
		}


####Ingresar Trabajador
class OperadorForm(forms.ModelForm):
	class Meta:
		model= Operador #Tabla a referenciar
		fields= ['rutOperador','nombreOperador','apellidoOperador','mailOperador','estadoOperador'] #atribitos a ingresar
		widgets={
				'rutOperador': forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder':'Rut','style':'width:50%'}),
				'nombreOperador': forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder':'Nombre','style':'width:50%'}),
				'apellidoOperador': forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder':'Apellido','style':'width:50%'}),
				'mailOperador': forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder':'Mail','style':'width:50%'}),
				'estadoOperador': forms.Select(attrs={'class':'form-control','placeholder':'Estado','style':'width:50%'})
			}

####Ingresar material nuevo 
class MaterialForm(forms.ModelForm):
	class Meta:
		model= Material #Tabla a referenciar
		fields= ['nombreMaterial','cantidad','unidadMedida','tipoMaterial'] #atributos a ingresar
		widgets={
				'nombreMaterial': forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder':'Nombre Material','style':'width:50%'}),
				'cantidad': forms.TextInput(attrs={'type':'number','class':'form-control col-sm-4','placeholder':'Cantidad','style':'width:50%'}),
				'unidadMedida': forms.Select(attrs={'class':'form-control','placeholder':'Unidad de Medida','style':'width:50%'}),
				'tipoMaterial': forms.Select(attrs={'class':'form-control','placeholder':'Tipo de Material','style':'width:50%'})
			}

#################################INTENTO AGREGAR USUARIOS

class UserForm(forms.ModelForm):
    ClaveRepetida = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control col-sm-4'}),required=True,label='Repita su clave')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control col-sm-4'}),required=True,label='Clave')
    class Meta:
        model = User
        fields = ('username', 'password',)
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control','placeholder': 'ej: 1234567-5'}),  
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
        }
