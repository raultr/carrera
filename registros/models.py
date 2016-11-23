from django.db.models.signals import pre_save, post_save
from django.core.exceptions import ValidationError,NON_FIELD_ERRORS
from django.db import models
from municipios.models import Municipio

class Registro(models.Model):
	paterno  = models.CharField(max_length=50, default='')
	materno  = models.CharField(max_length=50, default='')
	nombre   = models.CharField(max_length=50, default='')
	dia      = models.IntegerField(default=1)
	mes      = models.IntegerField(default=8)
	anio     = models.IntegerField(default=2016)
	genero   = models.CharField(max_length=1,default="",blank=True)
	cp       = models.CharField(max_length=10, default = '')
	estado   = models.CharField(max_length=7, default = '')
	email    = models.CharField(max_length=50,blank=True, default='')
	telefono = models.CharField(max_length=50,blank=True, default='')
	alergia  = models.CharField(max_length=50,blank=True, default='')
	duatlon  = models.CharField(max_length=50,blank=True, default='')
	ciclista = models.CharField(max_length=50,blank=True, default='')
	municipio = models.ForeignKey(Municipio,null=True, default=1,related_name='estado_municipio',on_delete=models.PROTECT)						
	email_ciclista = models.CharField(max_length=50,blank=True, default='')
	numero = models.IntegerField(default=1)
	

	# def unique_error_message(self, model_class, unique_check):
	# 	import ipdb;ipdb.set_trace()
	# 	if model_class == type(self) and unique_check == ('genero', 'email'):
	# 		return 'Your custom error message.'
	# 	else:
	# 		return super(Registro, self).unique_error_message(model_class, unique_check)

	
	# class Meta:
	# 	unique_together = ('genero', 'email',)

		#,error_messages={'unique':"Alguien ya fue registrado con ese email"}


	#def __str__(self):
	#	return self.paterno + ' ' + self.materno + ' ' + self.nombre

	def __unicode__(self):
		return u'{c}/{l}/{p}'.format(c=self.paterno, l=self.materno, p=self.nombre)

#./manage.py runserver --settings=carreras.settings