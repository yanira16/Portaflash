from django.conf.urls import include, url
from django.contrib import admin
from .views import *

urlpatterns = [
	#Admin Django
    url(r'^admin/', include(admin.site.urls)),

    #generales y sesion
    url(r'^$', Home("a").mostrarHome),
    url(r'^ordenesdecompra/listado/', oc_view, name= 'listado_oc'),
    url(r'^iniciosesion$', Login("a").mostrarLogin),
    url(r'^ModificarPerfil$', ModificarPerfil("a").mostrarModificarPerfil),
	url(r'^modificarContrasena$', ModificarContrasena("a").mostrarModificarContrasena),
	url(r'^logout/', logout_view, name= 'vista_logout'),

	#administrador
    url(r'^HomeAdmi$', HomeAdmi("a").mostrarHomeAdmi),
	url(r'^admitrab$', AdmiTrab("a").mostrarAdmiTrab),
	url(r'^admitrabingretrab$', AdmiTrabIngreTrab("a").mostrarAdmiTrabIngreTrab, name='vista_ingresar_trabajador'), #Ingresar trabajador
	url(r'^admitrabmodiestado_getForm$', AdmiTrabModiEstado_getForm, name="vista_modificar_trab_get_form"),#Modificar Trabajador
	url(r'^admitrabmodiestado$', AdmiTrabModiEstado("a").mostrarAdmiTrabModiEstado,name="vista_modificar_trab"),
	url(r'^admitrabmodtrab$', AdmiTrabModTrab("a").mostrarAdmiTrabModTrab),
	url(r'^admimaqui$', AdmiMaqui("a").mostrarAdmiMaqui),
	url(r'^admimaquiverestado$', AdmiMaquiVerEstado("a").mostrarAdmiMaquiVerEstado),
	url(r'^admimaquimodiestado$', AdmiMaquiModiEstado("a").mostrarAdmiMaquiModiEstado, name='vista_modificar_estado_maquinaria'),
	url(r'^admimaquiingremaqui$', AdmiMaquiIngreMaqui("a").mostrarAdmiMaquiIngreMaqui, name='vista_ingresar_maquinaria'), ###BASE PARA INGRESAR
	url(r'^admimaquimodiestado_getForm$', AdmiMaquiModiEstado_getForm, name="vista_modificar_maqui_get_form"), ##BASE MODIFICAR ESTADO
	url(r'^adminuevaorden$', AdmiOrdenIngre("a").mostrarAdmiOrdenIngre,name="vista_ingresar_orden"),


	#Bodeguero
	url(r'^HomeBode$', HomeBode("a").mostrarHomeBode),
	url(r'^bodenuevomate$', BodeNuevoMate("a").mostrarBodeNuevoMate, name='vista_nuevo_material'), ###Ingresar Material nuevo
	
	#Vendedor
	url(r'^HomeVende$', HomeVende("a").mostrarHomeVende),
	###COSAS AGREGADAS
	url(r'^vendgenerarOT$', vendgenerarOT("a").mostrarvendgenerarOT),
	url(r'^vendconsulOC$', vendconsulOC("a").mostrarvendconsulOC),
	url(r'^vendconsulOCverestadoOC$', vendconsulOCverestadoOC("a").mostrarvendconsulOCverestadoOC),
	url(r'^vendconsulOCverestadoavanceOC$', vendconsulOCverestadoavanceOC("a").mostrarvendconsulOCverestadoavanceOC),
	url(r'^vendadmiOC$', vendadmiOC("a").mostrarvendadmiOC),
	url(r'^vendadmiOCverOC$', vendadmiOCverOC("a").mostrarvendadmiOCverOC),
	url(r'^vendadmiOCmodificarOC$', vendadmiOCmodificarOC("a").mostrarvendadmiOCmodificarOC),


	

	#Jefe de Taller
	url(r'^HomeJefe$', HomeJefe("a").mostrarHomeJefe),
	###COSAS AGREGADAS
	url(r'^jefetallerasigtareas$', jefetallerasigtareas("a").mostrarjefetallerasigtareas),
	url(r'^jefetallerOF$', jefetallerOF("a").mostrarjefetallerOF),
	url(r'^jefetallerOFactualavanOF$', jefetallerOFactualavanOF("a").mostrarjefetallerOFactualavanOF),
	url(r'^jefetallerOFverestadoavanOF$', jefetallerOFverestadoavanOF("a").mostrarjefetallerOFverestadoavanOF),
	url(r'^jefetallerproductrab$', jefetallerproductrab("a").mostrarjefetallerproductrab),
	url(r'^jefetallerproductrabactualproduc$', jefetallerproductrabactualproduc("a").mostrarjefetallerproductrabactualproduc),
	url(r'^jefetallerproductrabverproduc$', jefetallerproductrabverproduc("a").mostrarjefetallerproductrabverproduc),



	
]
