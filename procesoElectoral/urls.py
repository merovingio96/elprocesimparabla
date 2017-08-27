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
    url(r'^agrupaciones/(?P<pk>[-\w]+)/edit/$', views.EditAgrupacion.as_view(success_url="/agrupaciones"), name='editar_agrupacion'),
    url(r'^agrupaciones/(?P<pk>[-\w]+)/$', views.DetailAgrupacion.as_view(), name='detalle_agrupacion'),
    url(r'^agrupaciones/(?P<pk>[-\w]+)/delete/$', views.DeleteAgrupacion.as_view(success_url="/agrupaciones"), name='delete_agrupacion'),
    url(r'^militantes/$', views.listMilitantes, name='militantes'),
    url(r'^militantes/new/$', views.addMilitante, name='anadir_militante'),
    url(r'^militantes/(?P<id_militante>[-\w]+)/$', views.detailMilitante, name='detalle_militante'),
    url(r'^militantes/(?P<id_militante>[-\w]+)/edit/$', views.editMilitante, name='editar_militante'),
    url(r'^militantes/(?P<id_militante>[-\w]+)/delete/$', views.deleteMilitante, name='eliminar_militante'),
]
