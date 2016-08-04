from django.conf.urls import patterns, url
from registros import views

urlpatterns =[
    url(r'^registro/$', views.RegistroLista.as_view(),name="registro_lista"),
	url(r'^registro/(?P<pk>[0-9]+)/$', views.RegistroIndividual.as_view(),name='registro_individual'),
 	 ]	