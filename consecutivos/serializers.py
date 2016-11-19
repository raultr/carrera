from rest_framework import serializers
from .models import Consecutivo

class ConsecutivoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Consecutivo
		fields = ('id','llave','valor_inicial','nombre_secuencia',)	