from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from django.db import transaction,IntegrityError
from django.db.models import Q
from .models import Registro
from consecutivos.models import Consecutivo
from .serializers import RegistroSerializer
from sequences import get_next_value

class RegistroDetalleMixin(object):
	queryset = Registro.objects.all()
	serializer_class = RegistroSerializer

class RegistroLista(RegistroDetalleMixin, ListCreateAPIView):
	def perform_create(self, serializer):
		with transaction.atomic():
			num_sig = Consecutivo.objects.get(llave=self.request.data['genero'])
			serializer.save(numero=get_next_value(num_sig.nombre_secuencia, initial_value=num_sig.valor_inicial))

class RegistroIndividual(RegistroDetalleMixin,RetrieveUpdateDestroyAPIView):
	pass

class RegistroDatosEmail(RegistroDetalleMixin,ListAPIView):
	def get_queryset(self):
		valor_buscado = self.kwargs['email_buscado'].strip()
		queryset=Registro.objects.filter(email=valor_buscado).exclude(duatlon='infantil')
		return queryset