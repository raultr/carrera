from django.shortcuts import render
from .models import Consecutivo
from .serializers import ConsecutivoSerializer
from rest_framework.views import APIView

class ConsecutivoDetalleMixin(object):
	queryset = Consecutivo.objects.all()
	serializer_class = ConsecutivoSerializer

class ConsecutivoLista(ConsecutivoDetalleMixin, ListCreateAPIView):
	pass

class ConsecutivoIndividual(ConsecutivoDetalleMixin,RetrieveUpdateDestroyAPIView):
	pass
