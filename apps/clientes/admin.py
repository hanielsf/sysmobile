# Django
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Cliente


# Register your models here.

@admin.register(Cliente)
class ClienteAdmin(ImportExportModelAdmin):
    list_display = (
        'cliente_id',
        'pes_nome',
        'pes_cpf',
    )
    pass

