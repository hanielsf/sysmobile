from django.db import models
from apps.core.models import Pessoa


#  ======================================== MODELO_CONTRATADO ================================================
class Cliente(Pessoa):
    #  basicas
    cliente_id = models.AutoField(db_column='cliente_id', auto_created=True, primary_key=True,
                                  unique=True, null=False, serialize=False)

    class Meta:
        ordering = ['pes_nome']
        db_table = 'CLIENTES'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.pes_nome


