# Django
from django.contrib import admin
from .models import Cliente


# Register your models here.

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'cliente_id',
        'pes_nome',
        'pes_cpf',
    )

