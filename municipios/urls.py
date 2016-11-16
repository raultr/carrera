from django.conf.urls import patterns, url
from municipios import views

urlpatterns =[
    url(r'^municipio/$', views.MunicipioLista.as_view(),name="municipio_lista"),
	url(r'^municipio/(?P<pk>[0-9]+)/$', views.MunicipioIndividual.as_view(),name='municipio_individual'),
	url(r'^municipio/estado/(?P<estado>[A-Za-z0-9.@\s]+)/$', views.MunicipiosPorEstado.as_view(),name="municipios_por_estado"),
 	 ]	