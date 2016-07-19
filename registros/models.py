from django.db import models

class Registro(models.Model):
	paterno  = models.CharField(max_length=50, default='')
	materno  = models.CharField(max_length=50, default='')
	nombre  = models.CharField(max_length=50, default='')

	def __str__(self):
		return self.paterno + ' ' + self.materno + ' ' + self.nombre