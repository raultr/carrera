from django.contrib import admin
from .models import Consecutivo
					
class ConsecutivoAdmin(admin.ModelAdmin):
	list_display =('id','llave','valor_inicial','nombre_secuencia')

admin.site.register(Consecutivo,ConsecutivoAdmin)


