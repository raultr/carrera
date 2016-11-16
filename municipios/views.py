from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from django.db import IntegrityError
from django.db.models import Q
from .models import Municipio
from .serializers import MunicipioSerializer

class MunicipioDetalleMixin(object):
	queryset = Municipio.objects.all()
	serializer_class = MunicipioSerializer

class MunicipioLista(MunicipioDetalleMixin, ListCreateAPIView):
	pass

class MunicipioIndividual(MunicipioDetalleMixin,RetrieveUpdateDestroyAPIView):
	pass

class MunicipiosPorEstado(MunicipioDetalleMixin,ListAPIView):
	def get_queryset(self):
		valor_buscado = self.kwargs['estado'].strip()
		queryset=Municipio.objects.filter(estado__iexact=valor_buscado)
		return queryset