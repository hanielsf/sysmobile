from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Dispositivo


# Register your models here.
@admin.register(Dispositivo)
class DispositivoAdmin(ImportExportModelAdmin):
    pass

