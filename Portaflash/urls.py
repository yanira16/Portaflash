from django.conf.urls import include, url
from django.contrib import admin
from .views import Home 

urlpatterns = [
    # Examples:
    # url(r'^$', 'Portaflash.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Home("a").mostrarHome),
]
