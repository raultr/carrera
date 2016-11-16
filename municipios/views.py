from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from django.db.models import Q
from .models import Municipio
from .serializers import MunicipioSerializer
from rest_framework.views import APIView

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

class MunicipioMasivo(APIView):
	def post(self, request, format=None):
		datos = request.data;
		serializer = MunicipioSerializer(data=request.data,many=True)
		if serializer.is_valid():
			try:
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			except IntegrityError as e:
				return Response({"La clave del municipio ya existe"}, status=status.HTTP_403_FORBIDDEN)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

