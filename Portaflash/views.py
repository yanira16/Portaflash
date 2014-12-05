from django.shortcuts import render
from django.views.generic import TemplateView
from models import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from Portaflash.forms import *
from django.views.decorators.csrf import csrf_exempt

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

class HomeBode(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarHomeBode(self,request):
		return render(request, 'Portaflash/homeBode.html',{})

class HomeVende(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarHomeVende(self,request):
		return render(request, 'Portaflash/homeVende.html',{})

class HomeJefe(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarHomeJefe(self,request):
		return render(request, 'Portaflash/homeJefe.html',{})

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

####BASE PARA INGRESAR
'''class AdmiMaquiIngreMaqui(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdmiMaquiIngreMaqui(self,request):
		form= MaquinariaForm(request.POST or None)
		if request.method=='POST':
			if form.is_valid():
				form.save()
				messages.success(request,'Se ha ingresado correctamente la maquinaria.')
				return HttpResponseRedirect("/admimaqui")
			else:
				messages.error(request,'Debe llenar correctamente todos los campos disponibles.')
		ctx= {'MaquinariaForm':form}
		return render(request, 'Portaflash/admimaquiingremaqui.html',ctx)'''


class AdmiMaquiIngreMaqui(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdmiMaquiIngreMaqui(self,request):
		form= MaquinariaForm(request.POST or None)
		if request.method=='POST':
			if form.is_valid():
				duplicidad = PuestoTrabajo.objects.filter(puestoTrabajo=request.POST["puestoTrabajo"])
				if len(duplicidad)==0:
					form.save()
					messages.success(request,'Se ha ingresado correctamente la maquinaria.')
					return HttpResponseRedirect("/admimaqui")
				else:
					messages.error(request, "Ya existe una maquinaria registrada con ese nombre.")
			else:
				messages.error(request,'Debe llenar todos los campos disponibles.')
		ctx= {'MaquinariaForm':form}
		return render(request, 'Portaflash/admimaquiingremaqui.html',ctx)


####Ingresar Operador
class AdmiTrabIngreTrab(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdmiTrabIngreTrab(self,request):
		form= OperadorForm(request.POST or None)
		if request.method=='POST':
			if form.is_valid():
				form.save()
				messages.success(request,'Se ha ingresado correctamente el trabajador.')
				return HttpResponseRedirect("/admitrab")
			else:
				messages.error(request,'Debe llenar correctamente todos los campos disponibles.')
		ctx= {'OperadorForm':form}
		return render(request, 'Portaflash/admitrabingretrab.html',ctx)



####Ingresar nuevo material
class BodeNuevoMate(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarBodeNuevoMate(self,request):
		form= MaterialForm(request.POST or None)
		if request.method=='POST':
			if not form.is_valid():
				form.save()
				messages.success(request,'Se ha ingresado correctamente el material.')
				return HttpResponseRedirect("Portaflash/homeBode")
			else:
				messages.error(request,'Debe llenar correctamente todos los campos disponibles.')
		ctx= {'MaterialForm':form}
		return render(request, 'Portaflash/bodenuevomate.html',ctx)


#######3Modificar Estado Maquina
class AdmiMaquiModiEstado(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdmiMaquiModiEstado(self,request):
		maquis = PuestoTrabajo.objects.all().order_by('puestoTrabajo')
		form = MaquinariaForm(request.POST or None)
		if request.method=='POST':
			if form.is_valid():
				maqui = PuestoTrabajo.objects.filter(puestoTrabajo=request.POST["puestoTrabajo"])[0]
				maqui.estadoMaquinaria = request.POST["estadoMaquinaria"]
				maqui.save()
				messages.success(request,'Se ha modificado correctamente el estado de la maquinaria.')
				return HttpResponseRedirect("/admimaqui")
			else:
				messages.error(request,'Valor incorrecto para el estado de la maquinaria')
		ctx = {'maquinarias':maquis,'MaquinariaForm':form}
		return render(request, 'Portaflash/admimaquimodiestado.html',ctx)

@csrf_exempt
def AdmiMaquiModiEstado_getForm(request):
	maqui = PuestoTrabajo.objects.get(pk=request.POST["id"])
	form = MaquinariaForm(instance=maqui)
	ctx={
		'MaquinariaForm':form,
	}
	return render(request, 'Portaflash/admimaquimodiestado_getForm.html',ctx)


###Ver Estado
class AdmiMaquiVerEstado(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdmiMaquiVerEstado(self,request):
		maquinarias = PuestoTrabajo.objects.all().order_by("puestoTrabajo")
		ctx = {"maquinarias":maquinarias}
		return render(request, 'Portaflash/admimaquiverestado.html',ctx)
		

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
					#roles = Rol.objects.filter(usuario=usuario).filter(rol=request.POST['rol'])
					if len(usuario)==1:
					#if len(usuario)==1 && len(roles)==1:
						request.session['ROL_USUARIO']= request.POST['rol']
						login(request, user)
						messages.success(request,'Bienvenido ' + usuario[0].nombreUsuario)
						return HttpResponseRedirect('/')
			messages.error(request,'Usuario o Contrasena incorrectos')
			return render(request, 'Portaflash/login.html',{})

def logout_view(request):
    """
    Cierra la sesion de un usuario y lo redirecciona al home
    """
    logout(request)
    return HttpResponseRedirect('/')

				