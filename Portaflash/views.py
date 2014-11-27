from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class Home(TemplateView):
	def __init__(self,valor):
		self.valor = valor
	def mostrarHome(self,request):
		context= {'pelicula':''}
		return render(request, 'Portaflash/home.html',context)