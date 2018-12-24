from django.contrib import admin
from django.contrib.auth.models import Group, User

from voyage.models import *


@admin.register(DocumentoViagem)
class DocumentoViagemAdmin(admin.ModelAdmin):
    add_form_template = 'admin/documento_viagem/documento_viagem_add_form.html'


admin.site.site_header = 'Site administrativo Voyage'
admin.site.register(Trajeto)
admin.site.register(Agente)
admin.site.register(Coordenador)
admin.site.register(TipoViagem)
admin.site.register(Cidade)

admin.site.unregister(Group)
admin.site.unregister(User)
