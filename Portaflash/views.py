from django.shortcuts import render
from django.views.generic import TemplateView
from models import *
from django.shortcuts import render_to_response
from django.template import RequestContext
# Create your views here.
class Home(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarHome(self,request):
		context= {'pelicula':''}
		return render(request, 'Portaflash/home.html',context)


#Lista todas las ordenes de compra de sistema
def oc_view(request):
	ordenes= OrdenDeCompra.objects.all()
	ctx ={'oc':ordenes}
	return render_to_response('Portaflash/oc.html',ctx,context_instance=RequestContext(request))

class Login(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarLogin(self,request):
		return render(request, 'Portaflash/login.html',{})
