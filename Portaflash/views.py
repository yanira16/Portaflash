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

class AdmiUsuario(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdmiUsuario(self,request):
		return render(request, 'Portaflash/admiusuario.html',{})

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

####Ingresar Usuario
class AdmiUsuarioIngreUsuario(TemplateView):
	def __init__(self,valor):
		self.valor = valor

	def mostrarAdmiUsuarioIngreUsuario(self,request):
		form= UsuarioForm()
		form2= UserForm()
		form3= RolForm()
		
		roles = {} 
		if "check-admi" in request.POST: 
			roles["admin"] = True 
		if "check-vende" in request.POST: 
			roles["vende"] = True 
		if "check-jefe" in request.POST: 
			roles["jefe"] = True 
		if "check-bode" in request.POST: 
			roles["bode"] = True
		form= UsuarioForm(request.POST or None)
		form2= UserForm(request.POST or None)
		if request.method=='POST':
			if form2.is_valid() and form.is_valid():
					password = form2.cleaned_data['password']
					username = form2.cleaned_data['username']
					user = User()
					user.username = username
					user.set_password(password)
					user.save()
					usuario= form.save(commit=False)
					usuario.user= user
					usuario.save()
					if "check-admi" in request.POST: 
						r = Rol(rol="Administrador", usuario= usuario) 
						r.save() 
					if "check-vende" in request.POST: 
						r = Rol(rol="Vendedor", usuario= usuario) 
						r.save()
					if "check-jefe" in request.POST: 
						r = Rol(rol="Jefe de Taller", usuario= usuario) 
						r.save() 
					if "check-bode" in request.POST: 
						r = Rol(rol="Bodeguero", usuario= usuario) 
						r.save()
											
					messages.success(request,'Se ha ingresado correctamente el usuario.')
					return HttpResponseRedirect("/admiusuario")
			else:
				messages.error(request,'Debe llenar correctamente todos los campos disponibles.')
		ctx= { 'UsuarioForm':form,'UserForm':form2, 'roles':roles}
		return render(request, 'Portaflash/admiusuarioingreusuario.html',ctx)



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



#######Modificar Estado Trabajador
class AdmiTrabModiEstado(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarAdmiTrabModiEstado(self,request):
		traba = Operador.objects.all().order_by('nombreOperador')
		form = OperadorForm(request.POST or None)
		if request.method=='POST':
			if "rutOperador" in request.POST:
				trab = Operador.objects.filter(pk=request.POST["rutOperador"])[0]
				trab.estadoOperador = request.POST["estadoOperador"]
				trab.mailOperador = request.POST["mailOperador"]
				trab.nombreOperador = request.POST["nombreOperador"]
				trab.apellidoOperador = request.POST["apellidoOperador"]
				trab.save()
				messages.success(request,'Se ha modificado correctamente el estado del trabajador.')
				return HttpResponseRedirect("/admitrab")
			else:
				messages.error(request,'Valor incorrecto para el estado del trabajador.')
		ctx = {'trabajadores':traba,'OperadorForm':form}
		return render(request, 'Portaflash/admitrabmodiestado.html',ctx)

@csrf_exempt
def AdmiTrabModiEstado_getForm(request):
	if "id" in request.POST and request.POST["id"]!="":
		trab = Operador.objects.get(pk=request.POST["id"])
		form = OperadorForm(instance=trab)
		ctx={
			'OperadorForm':form,
			'idOperador':request.POST["id"]
		}
		return render(request, 'Portaflash/admitrabmodiestado_getForm.html',ctx)
	else:
		return HttpResponse("")


####Ingresar nuevo material
class BodeNuevoMate(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarBodeNuevoMate(self,request):
		form= MaterialForm(request.POST or None)
		if request.method=='POST':
			if form.is_valid():
				form.save()
				messages.success(request,'Se ha ingresado correctamente el material.')
				return HttpResponseRedirect("/HomeBode")
				
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
					roles = Rol.objects.filter(usuario=usuario).filter(rol=request.POST['rol'])
					#if len(usuario)==1:
					if len(usuario)==1 and len(roles)>0:
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


class AdmiOrdenIngre(TemplateView):
	def __init__(self,valor):
		self.valor=valor
	def mostrarAdmiOrdenIngre(self, request):
		ctx = {}
		return render_to_response("Portaflash/admiordeningre.html", ctx, context_instance=RequestContext(request))


###COSAS AGREGADAS
class vendgenerarOT(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarvendgenerarOT(self,request):
		oc = OrdenDeCompra.objects.all()
		if request.method=='POST':
			orden= request.POST.get('generar')
		
			print 'id'

			ordenDeCompra= OrdenDeCompra.objects.get(id=orden)
			ordenDeTrabajo= OrdenTrabajo()
			ordenDeTrabajo.ordenDeCompra= ordenDeCompra
			user=User.objects.get(username=request.user.username)
			ordenDeTrabajo.usuario= user.usuario
			ordenDeTrabajo.save()

		ctx = {'ordenes':oc}
		return render(request, 'Portaflash/vendgenerarOT.html', ctx)

class VendeOrdenIngre(TemplateView):
	def __init__(self,valor):
		self.valor=valor
	def mostrarVendeOrdenIngre(self, request):
		numeroOrden = OrdenDeCompra.objects.all().order_by("-numeroOC")[:1][0].numeroOC+1
		productos   = TipoProducto.objects.all()
		terminacion = Terminacion.objects.all()
		vendedores  = Rol.objects.filter(rol="Vendedor")
		data={}
		if request.method == "POST":
			data["nombreEmpresa"]=request.POST["nombreEmpresa"]
			data["rutEmpresa"]=request.POST["rutEmpresa"]
			data["fechaIngreso"]=request.POST["fechaIngreso"]
			data["fechaEntrega"]=request.POST["fechaEntrega"]
			flag = True
			if request.POST["nombreEmpresa"]=="":
				messages.warning(request, "Nombre de empresa vacio.")
				flag = False
			if request.POST["rutEmpresa"]=="":
				messages.warning(request, "Rut de empresa vacio.")
				flag = False
			if request.POST["fechaIngreso"]=="":
				messages.warning(request, "Ingrese fecha ingreso.")
				flag = False
			if request.POST["fechaEntrega"]=="":
				messages.warning(request, "Ingrese fecha entrega.")
				flag = False
			if flag:
				#guardar
				vendedor = Usuario.objects.filter(user = request.user)[0]
				estado = Estado.objects.get(nombreEstado="Pendiente")
				oc = OrdenDeCompra(numeroOC=1, fechaIngreso=data["fechaIngreso"],fechaEntrega=data["fechaEntrega"] , nombreEmpresa=data["nombreEmpresa"], rutEmpresa= data["rutEmpresa"],usuario=vendedor,estado=estado, )
				oc.save()
				oc.numeroOC = oc.id+1020
				oc.save()
				data = request.POST["descripcionOC"][:-1].split("&")
				for det in data:
					valores = det.split("~")
					tipoProd = TipoProducto.objects.filter(pk=int(valores[0]))[0]
					term = Terminacion.objects.filter(pk=int(valores[2]))[0]
					p = Producto(cantidad=valores[3],descripcion=valores[1],ordenDeCompra=oc, tipoProducto=tipoProd)
					p.save()
					tp = TerminacionProducto(terminacion=term, producto=p)
					tp.save()
				messages.success(request, "Orden de compra registrada con exito")
				return HttpResponseRedirect("/vendadmiOC")
		ctx = {'vendedores':vendedores, 'terminacion':terminacion, 'productos':productos, 'data':data, 'numeroOrden':numeroOrden}
		return render_to_response("Portaflash/vendeordeningre.html", ctx, context_instance=RequestContext(request))

class vendconsulOC(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarvendconsulOC(self,request):
		return render(request, 'Portaflash/vendconsulOC.html',{})

class vendconsulOCverestadoOC(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarvendconsulOCverestadoOC(self,request):
		return render(request, 'Portaflash/vendconsulOCverestadoOC.html',{})

class vendconsulOCverestadoavanceOC(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarvendconsulOCverestadoavanceOC(self,request):
		return render(request, 'Portaflash/vendconsulOCverestadoavanceOC.html',{})

class vendadmiOC(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarvendadmiOC(self,request):
		return render(request, 'Portaflash/vendadmiOC.html',{})

class vendadmiOCmodificarOC(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarvendadmiOCmodificarOC(self,request):
		return render(request, 'Portaflash/vendadmiOCmodificarOC.html',{})

class vendadmiOCverOC(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarvendadmiOCverOC(self,request):
		return render(request, 'Portaflash/vendadmiOCverOC.html',{})

# COSAS AGREGADAS 2

class jefetallerasigtareas(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarjefetallerasigtareas(self,request):
		return render(request, 'Portaflash/jefetallerasigtareas.html',{})

class jefetallerOF(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarjefetallerOF(self,request):
		return render(request, 'Portaflash/jefetallerOF.html',{})



class jefetallerOFactualavanOF(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarjefetallerOFactualavanOF(self,request):
		otes=OrdenTrabajo.objects.all()
		return render(request, 'Portaflash/jefetallerOFactualavanOF.html',{'otes': otes})





class jefetallerOFverestadoavanOF(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarjefetallerOFverestadoavanOF(self,request):
		return render(request, 'Portaflash/jefetallerOFverestadoavanOF.html',{})

class jefetallerproductrab(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarjefetallerproductrab(self,request):
		return render(request, 'Portaflash/jefetallerproductrab.html',{})

class jefetallerproductrabactualproduc(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarjefetallerproductrabactualproduc(self,request):
		return render(request, 'Portaflash/jefetallerproductrabactualproduc.html',{})

class jefetallerproductrabverproduc(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarjefetallerproductrabverproduc(self,request):
		return render(request, 'Portaflash/jefetallerproductrabverproduc.html',{})


#######Bodeguero
class boderecepcionproducto(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarboderecepcionproducto(self,request):
		ordenes = OrdenDeCompra.objects.exclude(estado__nombreEstado="Despachada")
		ctx = {'ordenes':ordenes}
		return render(request, 'Portaflash/boderecepcionproducto.html',ctx)



@csrf_exempt
def boderecepcionproducto_getData(request):
	orden = OrdenDeCompra.objects.get(pk=request.POST["id"])
	ctx={
		'oc':orden
	}
	return render(request, 'Portaflash/boderecepcionproducto_getData.html',ctx)


#################################INTENTO AGREGAR USUARIOS
def registro_view(request):

	form_user = UserForm(request.POST or None) #Agregada
	#form_usuario = UsuarioForm(request.POST or None) #Agregada

	if request.POST:
		if form_user.is_valid() and form_usuario.is_valid():
			
			clave = form_user.cleaned_data['nombre'] #password y ClaveRepetida son los NAMES que tienen los inputs en el html
			clave2 = form_user.cleaned_data['nombre']
			if clave == clave2:
				if form_user.cleaned_data['username'] == '' or form_user.cleaned_data['username'] == None or clave == '' == '': # verifica que todos los campos obligatorios esten llenados
					messages.warning(request, "El nombre de usuario y clave no pueden ser nulos")
					HttpResponseRedirect("/admiusuario")
				else:
					usuarioo = User.objects.create_user(form_user.cleaned_data['username'],clave)
					usuarioo.save() #aqui se ingreso el usuario a la tabla de Django (auth_user)
			else:
				messages.warning(request,"Las claves ingresadas no coinciden")
				return HttpResponseRedirect("/admiusuario")		
		
			if form_socio.is_valid() and form_user.is_valid():
				usuario_inst = User.objects.get(username = form_user.cleaned_data['username']) #obtiene el user que ya se agrego, porke es necesario para crear el Usuario	
				if form_user.cleaned_data['nombre'] != "":
					#en la linea siguiente se crea el socio, los campos user, nacionalidad, nombre, etc son los atributos de Socio en el models, los valores entre comillas son los names que debiesen ser los mismos nombres si es ke se esta usando un modelForm
					usuario = Usuario(user=usuarioo_inst,username=form_user.cleaned_data['Username'],password=form_socio.cleaned_data['nombre'])
					usuario.save() #se crea el socio y se guarda
					messages.success(request,"El registro se ha realizado exitosamente")
					return HttpResponseRedirect('/')
				else:
					messages.warning(request,"El nombre de usuario no puede ser vacio")
					return HttpResponseRedirect('/registro')	
		messages.warning(request,"Error en los datos ingresados")
		return HttpResponseRedirect('/registro')							
	
	ctx = {'form_user': form_user,'form_usuario':form_socio}
	return render_to_response('Portaflash/admiordeningre.html', ctx, context_instance=RequestContext(request))


	###COSAS AGREGADAS 3

'''class bodeingremate(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarbodeingremate(self,request):
######################3


		form= MaterialForm(request.POST or None)
					if request.method=='POST':
						if form.is_valid():
							##################
							materialTemp = 
							aux = material.objects.get(tipo='materialTemp')
							aux.cantidad = aux.cantidad + nuevocantidad
							aux.save()
							###################
							form.save()
							messages.success(request,'Se ha ingresado correctamente el material.')
							return HttpResponseRedirect("/HomeBode")
							
						else:
							messages.error(request,'Debe llenar correctamente todos los campos disponibles.')
					ctx= {'MaterialForm':form}
		########################################3
		return render(request, 'Portaflash/bodeingremate.html',{})
'''



class bodeentregamate(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarbodeentregamate(self,request):
		return render(request, 'Portaflash/bodeentregamate.html',{})

class bodestock(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarbodestock(self,request):
		return render(request, 'Portaflash/bodestock.html',{})

###COSAS AGREGADAS 4

class admiadmiOC(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostraradmiadmiOC(self,request):
		return render(request, 'Portaflash/admiadmiOC.html',{})

class admiadmiOCverestadoOC(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostraradmiadmiOCverestadoOC(self,request):
		return render(request, 'Portaflash/admiadmiOCverestadoOC.html',{})

class admiadmiOCmodestadoOC(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostraradmiadmiOCmodestadoOC(self,request):
		return render(request, 'Portaflash/admiadmiOCmodestadoOC.html',{})

### HASTA AQUI
