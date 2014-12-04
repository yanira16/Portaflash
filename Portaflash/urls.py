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
	url(r'^admitrabingretrab$', AdmiTrabIngreTrab("a").mostrarAdmiTrabIngreTrab, name='vista_ingresar_trabajador'),
	url(r'^admitrabmodtrab$', AdmiTrabModTrab("a").mostrarAdmiTrabModTrab),
	url(r'^admitrabmodtrab$', AdmiTrabModTrab("a").mostrarAdmiTrabModTrab),
	url(r'^admimaqui$', AdmiMaqui("a").mostrarAdmiMaqui),
	url(r'^admimaquiverestado$', AdmiMaquiVerEstado("a").mostrarAdmiMaquiVerEstado),
	url(r'^admimaquimodiestado$', AdmiMaquiModiEstado("a").mostrarAdmiMaquiModiEstado, name='vista_modificar_estado_maquinaria'), ###BASE PARA IMODIFICAR
	url(r'^admimaquiingremaqui$', AdmiMaquiIngreMaqui("a").mostrarAdmiMaquiIngreMaqui, name='vista_ingresar_maquinaria'), ###BASE PARA INGRESAR

	url(r'^logout/', logout_view, name= 'vista_logout'),

	
]
