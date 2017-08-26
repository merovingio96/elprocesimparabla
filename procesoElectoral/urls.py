from django.conf.urls import url, include
import procesoElectoral.views as views
from .views import *
from .models import *

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^login/$', views.userLogin, name='login_usuario'),
    url(r'^logout/$', views.userLogout, name='logout_usuario'),
    url(r'^partidos/$', views.listPartidos, name='lista_de_partidos'),
    url(r'^partidos/new/$', views.addPartido, name='anadir_partido'),
    url(r'^partidos/(?P<id_partido>[-\w]+)/edit/$', views.editPartido, name='editar_partido'),
    url(r'^partidos/(?P<id_partido>[-\w]+)/delete/$', views.deletePartido, name='eliminar_partido'),
    url(r'^agrupaciones/$', views.ListAgrupaciones.as_view(), name='lista_de_agrupaciones'),
    url(r'^agrupaciones/new/$', views.AddAgrupacion.as_view(), name='anadir_agrupacion'),
    url(r'^agrupaciones/(?P<pk>[-\w]+)/edit/$', views.EditAgrupacion.as_view(model=Agrupacion, success_url="/agrupaciones"), name='editar_agrupacion'),
    url(r'^agrupaciones/(?P<pk>[-\w]+)/$', views.DetailAgrupacion.as_view(), name='detalle_agrupacion'),
    url(r'^militantes/$', views.goToMilitantes, name='militantes'),
    url(r'^militantes/new/$', views.addMilitante, name='anadir_militante'),
]
