# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
#from django.db.models.signals import post_save
#from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin
#from django.contrib.auth import authenticate, login


class Estado(models.Model):
	id= models.AutoField('id',primary_key=True)
	nombreEstado= models.CharField('Nombre Estado', max_length=256, null=False, blank=False)

	def __unicode__(self):
		return u'%s' % (self.nombreEstado)

class OrdenDeCompra(models.Model):
	numeroOC= models.IntegerField('Numero de Orden de Compra', primary_key=True)
	nombreEmpresa= models.CharField('Nombre Empresa', max_length=128, null=False, blank=False)
	rutEmpresa= models.CharField('Rut Empresa', max_length=10, null=False, blank=False)
	rutVendedor= models.CharField('Rut Vendedor', max_length=10, null=False, blank=False) #Proximamaente llave foranea
	fechaIngreso= models.DateField('Fecha Ingreso', null=False, blank=False)
	fechaEntrega= models.DateField('Fecha Entrega', null=False, blank=False)

	#LLaves Foraneas
	estado = models.ForeignKey(Estado,verbose_name="Estado")

	def __unicode__(self):
		return u'%s %s' % (self.numeroOC, self.fechaEntrega)

class Despacho(models.Model):
	id= models.AutoField('id',primary_key=True)
	fechaDespacho= models.DateField('Fecha Despacho', null=False, blank=False)

	#Llaves Foraneas
	ordenDeCompra = models.ForeignKey(OrdenDeCompra,verbose_name="Orden de Compra")

	def __unicode__(self):
		return u'%s' % (self.nombreEstado)

class Usuario(models.Model):
	rutUsuario= models.IntegerField('Rut Usuario', primary_key=True)
	nombreUsuario= models.CharField('Nombre Usuario', max_length=128, null=False, blank=False)
	apeliidoUsuario= models.CharField('Apellido Usuario', max_length=128, null=False, blank=False)
	rol= models.CharField('Rol Usuario', max_length=20, null=False, blank=False)

	#Llaves Foraneas
	user= models.OneToOneField(User) #Relacion uno a uno con la tabla usuario del sistema

