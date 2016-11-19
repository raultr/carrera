from django.db.models.signals import pre_save, post_save
from django.core.exceptions import ValidationError
from django.db import models

class Consecutivo(models.Model):
	llave 			  = models.CharField(max_length=7, default='')
	valor_inicial     = models.IntegerField(default=1)
	nombre_secuencia  = models.CharField(max_length=7, default='')


	def __unicode__(self):
		return u'{l}'.format(l=self.llave)