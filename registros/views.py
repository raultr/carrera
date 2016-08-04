from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.db.models import Q
from .models import Registro
from .serializers import RegistroSerializer

class RegistroDetalleMixin(object):
	queryset = Registro.objects.all()
	serializer_class = RegistroSerializer

class RegistroLista(RegistroDetalleMixin, ListCreateAPIView):
	pass

class RegistroIndividual(RegistroDetalleMixin,RetrieveUpdateDestroyAPIView):
	pass