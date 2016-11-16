from django.contrib import admin
from .models import Municipio
					
class MunicipioAdmin(admin.ModelAdmin):
	list_display =('id','estado','municipio',)

	search_fields = ('estado','municipio',) # Campos por los que se puede buscar, si son campos foraneos se usa campo__nomcampoforaneo

admin.site.register(Municipio,MunicipioAdmin)


