from __future__ import absolute_import
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from denuncias.views import pgprincipal, DenunciaCreate, contacto, listar, detail, check_pubs, listaDetalles, RegistroUsuario

urlpatterns = [
	url(r'^contacto', login_required(contacto), name='contacto'),
	url(r'^$', login_required(pgprincipal), name='pgprincipal'),
	url(r'^listar/', login_required(listar.as_view()), name='listar'),
	url(r'^crear/', login_required(DenunciaCreate.as_view()), name='denuncia_crear'),
	url(r'^(?P<denuncia_id>[0-9]+)/$', login_required(detail), name='detail'),
	url(r'^check_pubs/$', check_pubs, name='check_pubs'),
	url(r'^detalles/', listaDetalles, name='listaDetalles'),
	url(r'^registrar',RegistroUsuario.as_view(), name='registrar'),
]