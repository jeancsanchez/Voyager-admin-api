from django.contrib import admin
from django.contrib.admin import register

from voyage.models import *


@register(DocumentoViagem)
class DocumentoViagemAdmin(admin.ModelAdmin):
    pass


# admin.site.register(Rota)
# admin.site.register(Roteiro)
# admin.site.register(Destino)
# admin.site.register(Origem)
# admin.site.register(Status)
