from django.contrib.auth.models import User
from Portaflash.models import  Usuario
#from MP.forms import *



def datos_globales(request):
	if not request.user.is_anonymous():
		usuario = Usuario.objects.filter(user = request.user)
		if len(usuario) == 1:
			nombre = usuario[0].nombreUsuario
			if not 'ROL_USUARIO' in request.session:
				request.session['ROL_USUARIO']= 'Administrador'

			dict = {
				'NOMBRE_USUARIO':nombre,
				'NOMBRE_COMPLETO':nombre+" "+usuario[0].apellidoUsuario,
				'ROL_USUARIO':request.session['ROL_USUARIO']
			}
			return dict
	else:
		return {}
