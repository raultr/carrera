from rest_framework import serializers
from .models import Registro

class RegistroSerializer(serializers.ModelSerializer):
	class Meta:
		model = Registro
		fields = ('id','paterno','materno','nombre','dia','mes','anio','genero','cp','estado','municipio','email','telefono','alergia','duatlon','ciclista','email_ciclista','numero')
		