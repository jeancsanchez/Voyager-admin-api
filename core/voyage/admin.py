from django.contrib import admin
from django.contrib.admin import register
from django.contrib.auth.models import Group, User

from voyage.models import *

admin.site.site_header = 'Site administrativo Voyage'


@register(DocumentoViagem)
class DocumentoViagemAdmin(admin.ModelAdmin):
    readonly_fields = ['valor', ]
    list_display = ('solicitante', 'objetivo', 'valor')


admin.site.register(Trajeto)
admin.site.register(Agente)
admin.site.register(Coordenador)
admin.site.register(TipoViagem)
admin.site.register(Cidade)

admin.site.unregister(Group)
admin.site.unregister(User)
