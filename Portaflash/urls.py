from django.conf.urls import include, url
from django.contrib import admin
from .views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'Portaflash.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Home("a").mostrarHome),
    url(r'^ordenesdecompra/listado/', oc_view, name= 'listado_oc'),
    url(r'^iniciosesion$', Login("a").mostrarLogin),
    url(r'^HomeAdmi$', HomeAdmi("a").mostrarHomeAdmi),
    url(r'^ModificarPerfil$', ModificarPerfil("a").mostrarModificarPerfil),
	url(r'^modificarContrasena$', ModificarContrasena("a").mostrarModificarContrasena),
	url(r'^admitrab$', AdmiTrab("a").mostrarAdmiTrab),
	url(r'^admitrabingretrab$', AdmiTrabIngreTrab("a").mostrarAdmiTrabIngreTrab, name='vista_ingresar_trabajador'), #Ingresar trabajador
	url(r'^admitrabmodiestado_getForm$', AdmiTrabModiEstado_getForm, name="vista_modificar_trab_get_form"),#Modificar Trabajador
	url(r'^admitrabmodtrab$', AdmiTrabModTrab("a").mostrarAdmiTrabModTrab),
	url(r'^admitrabmodtrab$', AdmiTrabModTrab("a").mostrarAdmiTrabModTrab),
	url(r'^admimaqui$', AdmiMaqui("a").mostrarAdmiMaqui),
	url(r'^admimaquiverestado$', AdmiMaquiVerEstado("a").mostrarAdmiMaquiVerEstado),
	url(r'^admimaquimodiestado$', AdmiMaquiModiEstado("a").mostrarAdmiMaquiModiEstado, name='vista_modificar_estado_maquinaria'),
	url(r'^admimaquiingremaqui$', AdmiMaquiIngreMaqui("a").mostrarAdmiMaquiIngreMaqui, name='vista_ingresar_maquinaria'), ###BASE PARA INGRESAR
	url(r'^admimaquimodiestado_getForm$', AdmiMaquiModiEstado_getForm, name="vista_modificar_maqui_get_form"), ##BASE MODIFICAR ESTADO
	url(r'^HomeBode$', HomeBode("a").mostrarHomeBode),
	url(r'^bodenuevomate$', BodeNuevoMate("a").mostrarBodeNuevoMate, name='vista_nuevo_material'), ###Ingresar Material nuevo
	url(r'^HomeVende$', HomeVende("a").mostrarHomeVende),
	url(r'^HomeJefe$', HomeJefe("a").mostrarHomeJefe),

	url(r'^logout/', logout_view, name= 'vista_logout'),

	
]
