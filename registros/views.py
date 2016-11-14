from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from django.db import IntegrityError
from django.db.models import Q
from .models import Registro
from .serializers import RegistroSerializer

class RegistroDetalleMixin(object):
	queryset = Registro.objects.all()
	serializer_class = RegistroSerializer

class RegistroLista(RegistroDetalleMixin, ListCreateAPIView):
	pass
	# def create(self, request, *args, **kwargs):
	# try:
	# 	return super(ListCreateAPIView,self).create(request, *args, **kwargs)
	# except IntegrityError:
	# 	import ipdb;ipdb.set_trace()
	# 	return bad_request(request)
	# except Exception as e:
	# 	import ipdb;ipdb.set_trace()
	# 	return Response( e.args[0], status=status.HTTP_400_BAD_REQUEST)

class RegistroIndividual(RegistroDetalleMixin,RetrieveUpdateDestroyAPIView):
	pass

class RegistroDatosEmail(RegistroDetalleMixin,ListAPIView):
	def get_queryset(self):
		valor_buscado = self.kwargs['email_buscado'].strip()
		queryset=Registro.objects.filter(email=valor_buscado).exclude(duatlon='infantil')
		return queryset