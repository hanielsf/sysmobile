# Django
from django.utils.six import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models

# Local
from apps.core.models import TimeStamped, Displayable
from .choices import ACESSORIOS_DISPOSITIVOS, TIPO_SERVICOS, STATUS

# Terceiros
from simple_history.models import HistoricalRecords
from multiselectfield import MultiSelectField
from djmoney.models.fields import MoneyField
import qrcode


#  ======================================== MODELO_ORDEM_SERVICO ================================================
class OrdemServico(TimeStamped, Displayable):
    #  basicas
    os_id = models.AutoField(db_column='os_id', auto_created=True, primary_key=True,
                             unique=True, null=False, serialize=False)
    acessorios = MultiSelectField(choices=ACESSORIOS_DISPOSITIVOS, max_choices=4,
                                  db_column='acessorios', null=True, blank=True)
    tipo_servico = models.CharField(choices=TIPO_SERVICOS, db_column='tipo_servico', max_length=2)
    descricao = models.CharField(blank=True, null=True, max_length=300, db_column='descricao')
    status = models.CharField(choices=STATUS, db_column='status', max_length=1)
    orcamento = MoneyField(db_column='orcamento', max_digits=10, decimal_places=2,
                           default_currency='BRL', null=True, default=0,
                           blank=True)
    hospedagem = models.CharField(db_column='hospedagem', null=True, blank=True, max_length=4)

    # terceiros
    historico = HistoricalRecords()

    # relacionamentos
    cliente = models.ForeignKey('clientes.Cliente', on_delete=models.SET_NULL,
                                null=True, related_name="clientes")
    dispositivos = models.ForeignKey('dispositivos.Dispositivo', on_delete=models.SET_NULL,
                                     null=True, related_name="dispositivos")

    FECHADA = "FECHADA"

    class Meta:
        ordering = ['-os_id']
        db_table = 'ORDEMSERVICO'
        verbose_name = 'Ordem de Serviço'
        verbose_name_plural = 'Ordens de Serviço'

    def __str__(self):
        return "O.S: #" + str(self.os_id)



