from django.contrib import admin
from .models import Registro
					
class RegistroAdmin(admin.ModelAdmin):
	list_display =('id','paterno','materno','nombre','dia','mes','anio','genero','cp','estado','email','telefono','alergia','duatlon','ciclista','email_ciclista',)

	search_fields = ('paterno','materno','nombre') # Campos por los que se puede buscar, si son campos foraneos se usa campo__nomcampoforaneo

admin.site.register(Registro,RegistroAdmin)
