from django import forms
from registros.models import Registro

class RegistroForm(forms.ModelForm):
	class Meta:
		model = Registro
		fields = '__all__'