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
		exclude= ("user",)
		fields= ['rutUsuario','nombreUsuario','apellidoUsuario'] #atributos a ingresar
		widgets={
				'rutUsuario': forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder':'Rut','style':'width:50%'}),
				'nombreUsuario': forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder':'Nombre','style':'width:50%'}),
				'apellidoUsuario': forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder':'Apellido','style':'width:50%'}),
			}

class RolForm(forms.ModelForm):
	class Meta:
		model= Rol #Tabla a referenciar
		fields= ['rol'] #atributos a ingresar
		widgets={
				'rol': forms.Select(attrs={'class':'form-control','placeholder':'Rol','style':'width:50%'}),
				
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
    
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder': 'Username','style':'width:50%'}),  
            'password': forms.PasswordInput(attrs={'class':'form-control col-sm-4','placeholder': 'Password','style':'width:50%'}),
        }

class TipoProductoForm(forms.ModelForm):
	class Meta:
		model= TipoProducto #Tabla a referenciar
		fields= ['nombreTP',] #atributos a ingresar
		widgets={
				'nombreTP': forms.Select(attrs={'class':'form-control','placeholder':'Tipo de Producto','style':'width:50%'})
			}

class OrdenCompraForm(forms.ModelForm):
	class Meta:
		model= OrdenDeCompra #Tabla a referenciar
		fields= ['numeroOC'] #atributos a ingresar
		widgets={
				'numeroOC': forms.Select(attrs={'class':'form-control','placeholder':'Numero OC','style':'width:50%'}),
				
			}