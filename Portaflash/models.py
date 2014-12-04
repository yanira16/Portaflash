# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
#from django.db.models.signals import post_save
#from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin
#from django.contrib.auth import authenticate, login

Rol=(
	('Administrador', 'Administrador'),
	('Vendedor','Vendedor'),
	('Jefe de Taller', 'Jefe de Taller'),
	('Bodeguero', 'Bodeguero'),
	)

TipoProducto=(
	('Escalerrilla','Escalerrilla'),
	('Bandeja','Bandeja'),
	('Poste','Poste'),
	('Otro','Otro'),
	)

unidadMedida=(
	('Toneladas','Toneladas'),
	('Kilos','Kilos'),
	('Gramos','Gramos'),
	('Metros','Metros'),
	('Centimetros','Centimetros'),
	('Milimetros','Milimetros'),
	)

Estado=(
	('Pendiente','Pendiente'),
	('Aprobada','Aprobada'),
	('Despachada','Despachada'),
	)

EstadoOperador=(
	('Activo','Activo'),
	('Lincencia Medica','Lincencia Medica'),
	('Vacaciones','Vacaciones'),
	('Con Permiso','Con Permiso'),
	('Despedido','Despedido'),
	)

Terminacion=(
	('Zincado','Zincado'),
	('Galvanizado','Galvanizado'),
	('Pintura','Pintura'),
	)
EstadoMaquinaria=(
	('Activa','Activa'),
	('En Reparacion','En Reparacion'),
	('En Mantencion','En Mantencion'),
	('Desactivada','Desactivada'),
	)

#PuestoTrabajo=()
#Tarea=()
#Material=()



class Usuario(models.Model):
	rutUsuario= models.IntegerField('Rut Usuario', primary_key=True)
	nombreUsuario= models.CharField('Nombre Usuario', max_length=128, null=False, blank=False)
	apellidoUsuario= models.CharField('Apellido Usuario', max_length=128, null=False, blank=False)
	

	#Llaves Foraneas
	user= models.OneToOneField(User) #Relacion uno a uno con la tabla usuario del sistema

	def __unicode__(self):
		return u'%s %s' % (self.nombreUsuario,self.apellidoUsuario)


class Rol(models.Model):
	id= models.AutoField('id',primary_key=True)
	rol= models.CharField('Rol', max_length=20, null=False, blank=False, choices=Rol)

	#Llaves Foraneas
	usuario = models.ForeignKey(Usuario,verbose_name="Usuario")



class Estado(models.Model):
	id= models.AutoField('id',primary_key=True)
	nombreEstado= models.CharField('Nombre Estado', max_length=256, null=False, blank=False, choices=Estado)

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
	usuario = models.ForeignKey(Usuario,verbose_name="Usuario")

	def __unicode__(self):
		return u'%s %s' % (self.numeroOC, self.fechaEntrega)

class Despacho(models.Model):
	id= models.AutoField('id',primary_key=True)
	fechaDespacho= models.DateField('Fecha Despacho', null=False, blank=False)

	#Llaves Foraneas
	ordenDeCompra = models.ForeignKey(OrdenDeCompra,verbose_name="Orden de Compra")
	usuario = models.ForeignKey(Usuario,verbose_name="Usuario")

	def __unicode__(self):
		return u'%s' % (self.nombreEstado)


class TipoProducto(models.Model):
	id= models.AutoField('id',primary_key=True)
	nombreTP=models.CharField('Tipo de Producto', max_length=30, null=False, blank=False, choices=TipoProducto)

	def __unicode__(self):
		return u'%s' % (self.nombreTP)


class GrosorMaterial(models.Model):
	id= models.AutoField('id',primary_key=True)
	grosor= models.IntegerField('Grosor', max_length=5, null=False, blank=False)
	unidadMedida= models.CharField('Unidad de Medida', max_length=20, null=False, blank=False, choices=unidadMedida)

	def __unicode__(self):
		return u'%s' % (self.grosor)


class Dimension(models.Model):
	id= models.AutoField('id',primary_key=True)
	nombreDimension= models.CharField('Nombre Dimension', max_length=20, null=False, blank=False)
	medida= models.IntegerField('Medida', max_length=6, null=False, blank=False)
	unidadMedida= models.CharField('Unida de Medida', max_length=20, null=False, blank=False, choices=unidadMedida)

	def __unicode__(self):
		return u'%s' % (self.nombreDimension)


class Kilogramos(models.Model):
	id= models.AutoField('id',primary_key=True)
	kilos= models.IntegerField('Kilos', max_length=10, null=False, blank=False)

	#LLaves Foraneas
	tipoProducto = models.ForeignKey(TipoProducto,verbose_name="Tipo Producto")
	dimension = models.ForeignKey(Dimension,verbose_name="Dimension")
	grosorMaterial = models.ForeignKey(GrosorMaterial,verbose_name="Grosor Material")



class Producto(models.Model):
	id= models.AutoField('id',primary_key=True)
	cantidad= models.IntegerField('Cantidad', max_length=4, null=False, blank=False)
	descripcion= models.CharField('Descripcion', max_length=128, null=False, blank=False)

	#LLaves Foraneas
	tipoProducto = models.ForeignKey(TipoProducto,verbose_name="Tipo Producto")
	ordenDeCompra= models.ForeignKey(OrdenDeCompra,verbose_name="Orden de Compra")

	def __unicode__(self):
		return u'%s' % (self.tipoProducto)

class Terminacion(models.Model):
	id= models.AutoField('id',primary_key=True)
	nombreTerminacion= models.CharField('Terminacion', max_length=30, null=False, blank=False)


class TerminacionProducto(models.Model):
	id= models.AutoField('id',primary_key=True)

	#LLaves Foraneas
	terminacion = models.ForeignKey(Terminacion,verbose_name="Terminacion")
	producto = models.ForeignKey(Producto,verbose_name="Producto")


class Dimensiones(models.Model):
	id= models.AutoField('id',primary_key=True)
	nombreDimension= models.CharField('Dimension', max_length=20, null=False, blank=False)
	medida= models.IntegerField('Medida', max_length=6, null=False, blank=False)
	unidadMedida= models.CharField('Unidad de Medida', max_length=20, null=False, blank=False, choices=unidadMedida)

	#LLaves Foraneas
	producto = models.ForeignKey(Producto,verbose_name="Producto")


class OrdenTrabajo(models.Model):
	id= models.AutoField('id',primary_key=True)

	#Llaves Foraneas
	usuario = models.ForeignKey(Usuario,verbose_name="Usuario")
	ordenDeCompra = models.ForeignKey(OrdenDeCompra,verbose_name="Orden de Compra")

class PuestoTrabajo(models.Model): #Maquinaria
	id= models.AutoField('id',primary_key=True)
	puestoTrabajo=models.CharField('Maquinaria', max_length=20, null=False, blank=False)
	estadoMaquinaria= models.CharField('Estado', max_length=20, null=False, blank=False, choices=EstadoMaquinaria)

	def __unicode__(self):
		return u'%s' % (self.puestoTrabajo)

class Tarea(models.Model):
	id= models.AutoField('id',primary_key=True)
	tarea= models.CharField('Tarea', max_length=20, null=False, blank=False)

	#LLaves Foraneas
	puestoTrabajo = models.ForeignKey(PuestoTrabajo,verbose_name="Puesto de Trabajo")

	def __unicode__(self):
		return u'%s' % (self.tarea)


class Operador(models.Model):
	rutOperador= models.IntegerField('Rut', primary_key=True)
	nombreOperador= models.CharField('Nombre', max_length=20, null=False, blank=False)
	apellidoOperador= models.CharField('Apellido', max_length=20, null=False, blank=False)
	mailOperador= models.CharField('Mail', max_length=30, null=False, blank=False)
	estadoOperador= models.CharField('Estado', max_length=20, null=False, blank=False, choices=EstadoOperador)

	def __unicode__(self):
		return u'%s %s' % (self.nombreOperador, self.apellidoOperador)


class DetalleOT(models.Model):
	id= models.AutoField('id',primary_key=True)

	#Llaves Foraneas
	tarea = models.ForeignKey(Tarea,verbose_name="Tarea")
	operador = models.ForeignKey(Operador,verbose_name="Operador")
	ordenTrabajo = models.ForeignKey(OrdenTrabajo,verbose_name="Orden de Trabajo")


class OrdenTrabajoInterna(models.Model):
	id= models.AutoField('id',primary_key=True)


class Material(models.Model):
	id= models.AutoField('id',primary_key=True)
	nombreMaterial= models.CharField('Nombre Material', max_length=20, null=False, blank=False)

	def __unicode__(self):
		return u'%s' % (self.nombreMaterial)

class SemiElaborado(models.Model):
	id= models.AutoField('id',primary_key=True)
	cantidad= models.IntegerField('Cantidad', max_length=20, null=False, blank=False)
	unidadMedida= models.CharField('Unidad de Medida', max_length=20, null=False, blank=False, choices=unidadMedida)


class MateriaPrima(models.Model):
	id= models.AutoField('id',primary_key=True)
	cantidad= models.IntegerField('Cantidad', max_length=20, null=False, blank=False)
	unidadMedida= models.CharField('Unidad de Medida', max_length=20, null=False, blank=False, choices=unidadMedida)

class Composicion(models.Model):
	id= models.AutoField('id',primary_key=True)

	#Llaves Foraneas
	semiElaborado = models.ForeignKey(SemiElaborado,verbose_name="SemiElaborado")
	materiaPrima = models.ForeignKey(MateriaPrima,verbose_name="Materia Prima")


class OrdenTrabajoMaterial(models.Model):
	id= models.AutoField('id',primary_key=True)
	cantidad= models.IntegerField('Cantidad', max_length=20, null=False, blank=False)
	unidadMedida= models.CharField('Unidad de Medida', max_length=20, null=False, blank=False, choices=unidadMedida)
	
	#LLaves Foraneas
	ordenTrabajo = models.ForeignKey(OrdenTrabajo,verbose_name="Orden de Trabajo")
	ordenTrabajoInterna = models.ForeignKey(OrdenTrabajoInterna,verbose_name="Orden de Trabajo Interna")
	semiElaborado = models.ForeignKey(SemiElaborado,verbose_name="SemiElaborado")
	materiaPrima = models.ForeignKey(MateriaPrima,verbose_name="Materia Prima")

class Auditoria(models.Model):
	id= models.AutoField('id',primary_key=True)
	fechaModificacion= models.DateField('Fecha de Modificacion', max_length=10, null=False, blank=False) 
	tablaModificada= models.CharField('Tabla Modificada', max_length=20, null=False, blank=False)
	datosAntes= models.CharField('Datos Antes', max_length=128, null=False, blank=False)
	datosDespues= models.CharField('Datos Despues', max_length=128, null=False, blank=False)
	operacion= models.CharField('Operacion', max_length=35, null=False, blank=False)

	#Llaves Foraneas
	usuario = models.ForeignKey(Usuario,verbose_name="Usuario")