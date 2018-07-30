# Django
from django.db import models

# Local
from djmoney.models.fields import MoneyField
from apps.core.models import Pessoa, TimeStamped, Displayable
from .choices import *


#  ======================================== MODELO_CONTRATADO ================================================
class Contratado(Pessoa):
    #  basicas
    con_matricula = models.CharField(db_column='con_matricula', primary_key=True, max_length=30)
    estabelecimento = models.ForeignKey('empregador.Estabelecimento', on_delete=models.CASCADE)
    lotacao = models.ForeignKey('empregador.Lotacao', on_delete=models.CASCADE)
    funcao = models.ForeignKey('empregador.Funcao', on_delete=models.CASCADE)
    sindicato = models.ForeignKey('empregador.Sindicato', on_delete=models.CASCADE)

    #  trabalhistas
    con_tipo_reg_trabalhista = models.CharField(max_length=3, choices=TIPO_REGIME_TRABALHISTA,
                                                db_column='con_tipo_reg_trabalhista')
    con_tipo_reg_previdenciario = models.CharField(max_length=4, choices=TIPO_REGIME_PREVIDENCIARIO,
                                                   db_column='con_tipo_reg_previdenciario')
    con_regime_jornada = models.CharField(max_length=1, choices=REGIME_DE_JORNADA,
                                          db_column='con_regime_jornada')
    con_natureza_atividade = models.CharField(max_length=1, choices=NATUREZA_DA_ATIVIDADE,
                                              db_column='con_natureza_atividade')
    con_categoria = models.CharField(max_length=1, choices=CATEGORIA, db_column='con_categoria')

    #  info_contrato
    con_data_admissao = models.DateField(db_column='con_data_admissao', null=True, blank=True)
    con_tipo_contrato = models.CharField(db_column='con_tipo_contrato', max_length=1,
                                         blank=True, null=True, choices=TIPO_CONTRATO_TRABALHO)
    con_tipo_admissao = models.CharField(db_column='con_tipo_admissao', max_length=1,
                                         blank=True, null=True, choices=TIPO_ADMISSAO, default='A')
    con_unidade_salario = models.CharField(db_column='con_unidade_salario', max_length=1,
                                           choices=UNIDADE_SALARIO, default='M')
    con_indicativo_admissao = models.CharField(db_column='con_indicativo_admissao', max_length=1,
                                               choices=INDICATIVO_ADMISSAO, default='N')
    con_salario_mensal = MoneyField(db_column='con_salario_mensal', max_digits=10, decimal_places=2,
                                    default_currency='BRL', null=True,
                                    blank=True)
    con_calcular_dsr = models.BooleanField(db_column='con_calcular_dsr', default=True)
    con_receber_fgts = models.BooleanField(db_column='con_receber_fgts', default=True)

    #  outra empresa
    con_vinculo_outra_empresa = models.CharField(max_length=1, db_column='con_vinculo_outra_empresa',
                                                 null=True, blank=True, choices=VINCULO_COM_OUTRA_EMPRESA)
    con_cnpj_outra_empresa = models.CharField(max_length=14, db_column='con_cnjp_outra_empresa', null=True, blank=True)
    con_remuneracao_outra_empresa = MoneyField(db_column='con_remuneracao_outra_empresa', max_digits=10,
                                               decimal_places=2, default_currency='BRL', null=True, blank=True)

    class Meta:
        ordering = ['-con_matricula']
        db_table = 'CONTRATADOS'
        verbose_name = 'Contratado'
        verbose_name_plural = 'Contratados'

    def __str__(self):
        return self.pes_nome


class PessoaResumo(Pessoa):
    class Meta:
        proxy = True
        verbose_name = 'Pessoa Resumo'
        verbose_name_plural = 'Resumo de Pessoas'


