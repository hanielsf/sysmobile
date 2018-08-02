from time import timezone

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.servicos.DefaultFilterMixin import DefaultFilterMixin
from .models import OrdemServico
# Register your models here.


@admin.register(OrdemServico)
class OrdemServicoAdmin(DefaultFilterMixin, ImportExportModelAdmin):
    date_hierarchy = 'created_at'

    list_display = (
        'os_id',
        'status',
        'hospedagem',
    )
    list_select_related = (
        'cliente',
        'dispositivos',
    )
    readonly_fields = (
        'cliente',
        'dispositivos',
    )

    def get_default_filters(request):
        now = timezone.now()
        return {
            'created_at__year': now.year,
            'created_at__month': now.month,
        }

    pass


