from django.conf.urls import patterns, url
from registros import views

urlpatterns =[
    url(r'^registro/$', views.RegistroLista.as_view(),name="registro_lista"),
	url(r'^registro/(?P<pk>[0-9]+)/$', views.RegistroIndividual.as_view(),name='registro_individual'),
	url(r'^registro/email_adulto/(?P<email_buscado>[\w.@+-]+)/(?P<carrera>[A-Za-z0-9.@\s]+)/$', views.RegistroDatosEmail.as_view(),name="registro_datos_email"),
 	 ]	