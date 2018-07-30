# Django
from django.db import models

# Local
from apps.core.models import TimeStamped, Displayable
from .choices import MARCA_DISPOSITIVOS


#  ======================================== MODELO_CONTRATADO ================================================
class Dispositivo(TimeStamped, Displayable):
    #  basicas
    disp_id = models.AutoField(db_column='disp_id', auto_created=True, primary_key=True,
                               unique=True, null=False, serialize=False)
    marca = models.CharField(choices=MARCA_DISPOSITIVOS, max_length=3, db_column='marca')
    modelo = models.CharField(db_column='modelo', max_length=25)
    imei = models.CharField(db_column='imei', max_length=15, blank=True, null=True)
    url_img = models.ImageField(db_column='url_img', blank=True, upload_to='static/img/dispositivos/', null=True)
    cliente = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ['-disp_id']
        db_table = 'DISPOSITIVOS'
        verbose_name = 'Dispositivo'
        verbose_name_plural = 'Dispositivos'

    def __str__(self):
        return self.modelo


