from django.db import models

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
	email_ciclista = models.CharField(max_length=50,blank=True, default='')

	def __str__(self):
		return self.paterno + ' ' + self.materno + ' ' + self.nombre