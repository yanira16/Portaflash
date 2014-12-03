from django.shortcuts import render
from django.views.generic import TemplateView
from models import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages

# Create your views here.
class Home(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarHome(self,request):
		context= {'pelicula':''}
		return render(request, 'Portaflash/home.html',context)

class HomeAdmi(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarHomeAdmi(self,request):
		return render(request, 'Portaflash/homeAdmi.html',{})

class ModificarPerfil(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarModificarPerfil(self,request):
		return render(request, 'Portaflash/modificarPerfil.html',{})

class ModificarContrasena(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarModificarContrasena(self,request):
		return render(request, 'Portaflash/modificarContrasena.html',{})

class AdmiTrab(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdmiTrab(self,request):
		return render(request, 'Portaflash/admitrab.html',{})

class AdmiTrabIngreTrab(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdmiTrabIngreTrab(self,request):
		return render(request, 'Portaflash/admitrabingretrab.html',{})

class AdmiTrabModTrab(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdmiTrabModTrab(self,request):
		return render(request, 'Portaflash/admitrabmodtrab.html',{})

class AdmiMaqui(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdmiMaqui(self,request):
		return render(request, 'Portaflash/admimaqui.html',{})

class AdmiMaquiVerEstado(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdmiMaquiVerEstado(self,request):
		return render(request, 'Portaflash/admimaquiverestado.html',{})

class AdmiMaquiModiEstado(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdmiMaquiModiEstado(self,request):
		return render(request, 'Portaflash/admimaquimodiestado.html',{})

#Lista todas las ordenes de compra de sistema
def oc_view(request):
	ordenes= OrdenDeCompra.objects.all()
	ctx ={'oc':ordenes}
	return render_to_response('Portaflash/oc.html',ctx,context_instance=RequestContext(request))

class Login(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarLogin(self,request):
		if not request.method == 'POST': #Solicitud a la pagina por un formulario
			if not request.user.is_anonymous():
				return HttpResponseRedirect('/')
			return render(request, 'Portaflash/login.html',{})
		else:
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					usuario= Usuario.objects.filter(user=user)
					if len(usuario)==1:
						login(request, user)
						messages.success(request,'Bienvenido ' + usuario[0].nombreUsuario)
						return HttpResponseRedirect('/')
			messages.error(request,'Usuario o Contrasena incorrectos')
			return render(request, 'Portaflash/login.html',{})

				