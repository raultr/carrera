from django.db.models.signals import pre_save, post_save
from django.core.exceptions import ValidationError
from django.db import models

class Municipio(models.Model):
	estado  = models.CharField(max_length=7, default='')
	municipio  = models.CharField(max_length=100, default='')


	def __unicode__(self):
		return u'{m}'.format(m=self.municipio)