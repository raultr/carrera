from django.contrib import admin
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportMixin,ImportExportModelAdmin,ImportExportActionModelAdmin,ExportMixin,ExportActionModelAdmin
from import_export import fields,resources
from municipios.models import Municipio
from .models import Registro
					
class RegistroAdmin(resources.ModelResource):
	nmunicipio = fields.Field(column_name='nmunicipio', attribute='municipio', widget=ForeignKeyWidget(Municipio, 'municipio')) 

	class Meta: 
		model = Registro
		fields =('id','numero','paterno','materno','nombre','dia','mes','anio','genero','cp','estado','nmunicipio','email','telefono','alergia','duatlon','ciclista','email_ciclista',)
		export_order = ('numero','id','paterno','materno','nombre','dia','mes','anio','genero','cp','estado','nmunicipio','email','telefono','alergia','duatlon','ciclista','email_ciclista',)

	list_display =('id','numero','paterno','materno','nombre','dia','mes','anio','genero','cp','estado','municipio','email','telefono','alergia','duatlon','ciclista','email_ciclista',)

	search_fields = ('paterno','materno','nombre','numero') # Campos por los que se puede buscar, si son campos foraneos se usa campo__nomcampoforaneo

class RegistroAdminModel(ImportExportActionModelAdmin):
	resource_class = RegistroAdmin
	list_display =('id','numero','paterno','materno','nombre','dia','mes','anio','genero','cp','estado','municipio','email','telefono','alergia','duatlon','ciclista','email_ciclista',)

admin.site.register(Registro,RegistroAdminModel)